from django.contrib import admin

from .models import ArticleVoteEntity, VotingUserEntity

admin.site.register(ArticleVoteEntity)
admin.site.register(VotingUserEntity)