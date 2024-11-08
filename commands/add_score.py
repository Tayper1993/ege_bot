from sqlalchemy.ext.asyncio import AsyncSession

from core.models.score import Score


class AddScoreCommand:
    def __init__(self, student_id: int, subject_id: id, score: int, session: AsyncSession):
        self.student_id = student_id
        self.subject_id = subject_id
        self.score = score
        self.session = session

    async def execute(self):
        add_score = Score(
            student_id=self.student_id,
            subject_id=self.subject_id,
            score=self.score,
        )
        self.session.add(add_score)
        await self.session.commit()
