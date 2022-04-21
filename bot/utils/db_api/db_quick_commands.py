from sqlalchemy.exc import PendingRollbackError, IntegrityError

from bot.utils.db_api.schemas.user import session, User


def register_user(message):
    username = message.from_user.username if message.from_user.username else None
    user = User(id=int(message.from_user.id), username=username, name=message.from_user.full_name)

    session.add(user)

    try:
        session.commit()
        return True
    except IntegrityError:
        session.rollback()  # откатываем session.add(user)
        return False


def select_user(user_id):
    user = session.query(User).filter(User.id == user_id).first()
    return user
