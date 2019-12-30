"""empty message

Revision ID: 07a8a00735d1
Revises: 
Create Date: 2019-12-30 23:28:39.091814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07a8a00735d1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('admin_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('admin_name', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('admin_id'),
    sa.UniqueConstraint('admin_name')
    )
    op.create_table('batch',
    sa.Column('batch_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('batch_name', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('batch_id'),
    sa.UniqueConstraint('batch_name')
    )
    op.create_table('objective_type',
    sa.Column('objective_type_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('objective_type', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('objective_type_id'),
    sa.UniqueConstraint('objective_type')
    )
    op.create_table('student',
    sa.Column('student_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('student_name', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('student_id')
    )
    op.create_table('teacher',
    sa.Column('teacher_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('teacher_name', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('teacher_id')
    )
    op.create_table('test_type',
    sa.Column('type_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('test_type_name', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('type_id'),
    sa.UniqueConstraint('test_type_name')
    )
    op.create_table('todo',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('todo_item', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('section',
    sa.Column('section_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('section_name', sa.String(length=250), nullable=False),
    sa.Column('batch_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['batch_id'], ['batch.batch_id'], ),
    sa.PrimaryKeyConstraint('section_id'),
    sa.UniqueConstraint('section_name')
    )
    op.create_table('quizset',
    sa.Column('test_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('test_name', sa.String(length=250), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=False),
    sa.Column('time_full_test', sa.String(length=250), nullable=False),
    sa.Column('test_type_id', sa.Integer(), nullable=False),
    sa.Column('student_section_id', sa.Integer(), nullable=False),
    sa.Column('student_batch_id', sa.Integer(), nullable=False),
    sa.Column('flag_publish_test', sa.Boolean(), nullable=True),
    sa.Column('flag_jumble_question', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['student_batch_id'], ['batch.batch_id'], ),
    sa.ForeignKeyConstraint(['student_section_id'], ['section.section_id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teacher.teacher_id'], ),
    sa.ForeignKeyConstraint(['test_type_id'], ['test_type.type_id'], ),
    sa.PrimaryKeyConstraint('test_id'),
    sa.UniqueConstraint('test_name')
    )
    op.create_table('objective_questions',
    sa.Column('question_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('question', sa.Text(), nullable=False),
    sa.Column('option_1', sa.Text(), nullable=True),
    sa.Column('option_2', sa.Text(), nullable=True),
    sa.Column('option_3', sa.Text(), nullable=True),
    sa.Column('option_4', sa.Text(), nullable=True),
    sa.Column('answer', sa.Text(), nullable=False),
    sa.Column('marks', sa.Integer(), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=False),
    sa.Column('quiz_test_id', sa.Integer(), nullable=False),
    sa.Column('objective_type_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['objective_type_id'], ['objective_type.objective_type_id'], ),
    sa.ForeignKeyConstraint(['quiz_test_id'], ['quizset.test_id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teacher.teacher_id'], ),
    sa.PrimaryKeyConstraint('question_id')
    )
    op.create_table('subjective_questions',
    sa.Column('question_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('question', sa.Text(), nullable=False),
    sa.Column('answer', sa.Text(), nullable=False),
    sa.Column('marks', sa.Integer(), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=False),
    sa.Column('quiz_test_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['quiz_test_id'], ['quizset.test_id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teacher.teacher_id'], ),
    sa.PrimaryKeyConstraint('question_id')
    )
    op.create_table('submission_objective',
    sa.Column('submission_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('response', sa.Text(), nullable=True),
    sa.Column('marks', sa.Integer(), nullable=False),
    sa.Column('submission_time', sa.DateTime(), nullable=True),
    sa.Column('quiz_test_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['objective_questions.question_id'], ),
    sa.ForeignKeyConstraint(['quiz_test_id'], ['quizset.test_id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.student_id'], ),
    sa.PrimaryKeyConstraint('submission_id')
    )
    op.create_table('submission_subjective',
    sa.Column('submission_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('response', sa.Text(), nullable=True),
    sa.Column('marks', sa.Integer(), nullable=True),
    sa.Column('quiz_test_id', sa.Integer(), nullable=False),
    sa.Column('submission_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['question_id'], ['subjective_questions.question_id'], ),
    sa.ForeignKeyConstraint(['quiz_test_id'], ['quizset.test_id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.student_id'], ),
    sa.PrimaryKeyConstraint('submission_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('submission_subjective')
    op.drop_table('submission_objective')
    op.drop_table('subjective_questions')
    op.drop_table('objective_questions')
    op.drop_table('quizset')
    op.drop_table('section')
    op.drop_table('todo')
    op.drop_table('test_type')
    op.drop_table('teacher')
    op.drop_table('student')
    op.drop_table('objective_type')
    op.drop_table('batch')
    op.drop_table('admin')
    # ### end Alembic commands ###
