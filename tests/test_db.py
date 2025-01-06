from dataclasses import asdict

from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        user = User(
            username='Renan', email='test@test.com', password='minha_senha'
        )

        session.add(user)
        session.commit()

    user = session.scalar(select(User).where(User.email == 'test@test.com'))

    assert asdict(user) == {
        'id': 1,
        'username': 'Renan',
        'password': 'minha_senha',
        'email': 'test@test.com',
        'created_at': time,
        'updated_at': time,
    }
