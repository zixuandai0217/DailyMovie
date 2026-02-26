from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel
from typing import List, Optional
import hashlib

from app.models.database import get_db
from app.models.user import User, UserPreference, Favorite

router = APIRouter(prefix="/user", tags=["User"])

class WeChatLoginRequest(BaseModel):
    code: str
    userInfo: Optional[dict] = None

class UserPreferenceUpdate(BaseModel):
    genres: List[int] = []
    decades: List[str] = []
    keywords: Optional[str] = ""

class UserResponse(BaseModel):
    id: int
    nickname: Optional[str]
    avatar_url: Optional[str]
    preferences: Optional[dict] = None

@router.post("/login")
async def wechat_login(login_data: WeChatLoginRequest, db: AsyncSession = Depends(get_db)):
    # Mock WeChat OpenID generation (In production, call WeChat API)
    # Using code to generate a deterministic openid for testing
    openid = hashlib.md5(login_data.code.encode()).hexdigest()
    
    # Check if user exists
    result = await db.execute(select(User).where(User.openid == openid))
    user = result.scalars().first()
    
    if not user:
        # Create new user
        user = User(
            openid=openid,
            nickname=login_data.userInfo.get("nickName") if login_data.userInfo else "User_" + openid[:6],
            avatar_url=login_data.userInfo.get("avatarUrl") if login_data.userInfo else ""
        )
        db.add(user)
        await db.commit()
        await db.refresh(user)
        
        # Create default preferences
        pref = UserPreference(user_id=user.id)
        db.add(pref)
        await db.commit()
    
    # Get preferences
    pref_result = await db.execute(select(UserPreference).where(UserPreference.user_id == user.id))
    pref = pref_result.scalars().first()
    
    return {
        "token": openid, # Simple token for now
        "user": {
            "id": user.id,
            "nickname": user.nickname,
            "avatar_url": user.avatar_url,
            "preferences": {
                "genres": pref.genres if pref else [],
                "decades": pref.decades if pref else [],
                "keywords": pref.keywords if pref else ""
            }
        }
    }

@router.get("/profile")
async def get_profile(token: str, db: AsyncSession = Depends(get_db)):
    # Simple auth by openid token
    result = await db.execute(select(User).where(User.openid == token))
    user = result.scalars().first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
        
    pref_result = await db.execute(select(UserPreference).where(UserPreference.user_id == user.id))
    pref = pref_result.scalars().first()
    
    return {
        "id": user.id,
        "nickname": user.nickname,
        "avatar_url": user.avatar_url,
        "preferences": {
            "genres": pref.genres if pref else [],
            "decades": pref.decades if pref else [],
            "keywords": pref.keywords if pref else ""
        }
    }

@router.put("/preferences")
async def update_preferences(token: str, prefs: UserPreferenceUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.openid == token))
    user = result.scalars().first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    pref_result = await db.execute(select(UserPreference).where(UserPreference.user_id == user.id))
    pref = pref_result.scalars().first()
    
    if not pref:
        pref = UserPreference(user_id=user.id)
        db.add(pref)
    
    pref.genres = prefs.genres
    pref.decades = prefs.decades
    pref.keywords = prefs.keywords
    
    await db.commit()
    
    return {"status": "success"}
