from . import regex_patterns
from dataclasses import dataclass
from ..boxes.Sentence import Sentence
from ..boxes.Row import Row
from enum import Enum
from typing import List, Mapping, Any


class LineType(Enum):
    comment = 1
    content = 2


@dataclass
class ParsedLine:
    type: LineType
    data: Mapping[str, Any]


class ConnluParser:
    @classmethod
    def parse(cls, path: str, lang_code, ignore_compound_indexes=False) -> List[Sentence]:
        sentences: List[Sentence] = []
        sentence = Sentence(rows=[], sent_id=None, text=None,
                            lang_code=lang_code, sent_id_eng=None, text_eng=None)
        with open(path, 'r', encoding="utf-8") as file:
            for line in file:
                if not regex_patterns.ANY_NON_WHITESPACE.match(line):
                    # Empty line encountered, meaning sentence is over
                    if sentence != None and len(sentence.rows) > 0:
                        if sentence.lang_code == "eng":
                            sentence.sent_id_eng = sentence.sent_id
                        sentences.append(sentence)
                    sentence = Sentence(rows=[], sent_id=None, text=None,
                                        lang_code=lang_code, sent_id_eng=None, text_eng=None)
                    continue
                parsed_line = cls.__parse_line(line)
                cls.__update_sentence(
                    sentence, parsed_line, ignore_compound_indexes=ignore_compound_indexes)
        return sentences

    @classmethod
    def __parse_line(cls, line: str) -> ParsedLine:
        if regex_patterns.COMMENT_LINE.match(line):
            _, comment = line.split('#', 1)
            try:
                key, value = regex_patterns.EQUAL_SIGN_SPLITTER.split(
                    comment, 1)
                return ParsedLine(type=LineType.comment, data={"key": key, "value": value})
            except Exception as e:
                # malformed comment line
                return
        elif regex_patterns.CONTENT_LINE.match(line):
            row = Row.from_line(line)
            return ParsedLine(type=LineType.content, data={"row": row})
        else:
            raise ValueError("Line is not a comment or content line")

    @classmethod
    def __update_sentence(cls, sentence: Sentence, parsed_line: ParsedLine, ignore_compound_indexes=False):
        if not parsed_line:
            return
        if parsed_line.type == LineType.comment:
            key = parsed_line.data["key"].strip()
            value = parsed_line.data["value"].strip()
            if key == "sent_id":
                sentence.sent_id = value
            elif key == "text":
                sentence.text = value
            elif key == "sent_id_eng":
                sentence.sent_id_eng = value
            elif key == "text_eng":
                sentence.text_eng = value
        elif parsed_line.type == LineType.content:
            has_compound_index = regex_patterns.COMPOUND_INDEX.match(
                parsed_line.data["row"].index)
            if ignore_compound_indexes and has_compound_index:
                return
            sentence.rows.append(parsed_line.data["row"])
