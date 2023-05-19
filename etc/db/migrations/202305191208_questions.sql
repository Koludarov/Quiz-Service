-- migrate:up


CREATE TABLE questions (
  id SERIAL PRIMARY KEY,
  question_id INTEGER,
  question_text TEXT,
  answer_text TEXT,
  created_at TIMESTAMPTZ
);


CREATE UNIQUE INDEX question_id on questions(question_id);
CREATE INDEX questions_id_question on questions(question_id, question_text);


-- migrate:down


DROP TABLE questions CASCADE;
