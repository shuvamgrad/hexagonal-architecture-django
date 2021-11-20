from myapp.application.domain.model.article_vote import ArticleVote
from myapp.application.domain.model.identifier.article_id import ArticleId
from myapp.application.domain.model.identifier.user_id import UserId
from myapp.application.domain.model.vote import Vote
from tests.test_myapp.application.domain.model.identifier.article_id_creation import \
    create_article_id
from tests.test_myapp.application.domain.model.identifier.user_id_creation import \
    create_user_id


def build_article_vote(
    user_id: UserId = None,
    article_id: ArticleId = None,
    vote: Vote = Vote.UP
) -> ArticleVote:
    user_id = user_id or create_user_id()
    article_id = article_id or create_article_id()

    return ArticleVote(
        user_id=user_id,
        article_id=article_id,
        vote=vote
    )


