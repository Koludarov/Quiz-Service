-- migrate:up


CREATE TABLE questions (
  id SERIAL PRIMARY KEY,
  question_text TEXT,
  answer_text TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW()
);


CREATE UNIQUE INDEX question_text on questions(question_text);
CREATE INDEX questions_question_answer on questions(question_text, answer_text);


-- migrate:down


DROP TABLE questions CASCADE;
