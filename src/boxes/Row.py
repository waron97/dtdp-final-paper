from dataclasses import dataclass
from typing import Mapping, Any


@dataclass
class Row:
    index: str
    token: str
    lemma: str
    pos: str
    head_index: int
    rel_type: str
    attrs: Mapping[str, str]

    @classmethod
    def from_line(cls, line: str):
        split = line.split('\t')
        index = split[0]
        token = split[1]
        lemma = split[2]
        pos = split[3]
        attrs = cls.__parse_attrs(split[5])
        head_index = int(split[6]) if split[6] != "_" else None
        rel_type = split[7]

        return cls(index=index, token=token, lemma=lemma, pos=pos, head_index=head_index, rel_type=rel_type, attrs=attrs)

    def to_dict(self, include_attrs=False) -> Mapping[str, Any]:
        d = {
            "index": self.index,
            "token": self.token,
            "lemma": self.lemma,
            "pos": self.pos,
            "head_index": self.head_index,
            "rel_type": self.rel_type,
        }
        if include_attrs:
            d["attrs"] = self.attrs
        return d

    @classmethod
    def __parse_attrs(cls, attrs: str):
        ATTR_FIELDS = [
            "Case",
            "Number",
            "Person",
            "Tense",
            "VerbForm",
            "Voice",
            "SpaceAfter",
            "VerbForm",
            "PronType",
            "Number[psor]",
            "Person[psor]",
            "NumType",
            "Aspect",
            "VerbType"
        ]
        parsed = {
            key: None for key in ATTR_FIELDS
        }
        split = attrs.split('|')
        for attr in split:
            try:
                key, value = attr.split("=")
                parsed[key] = value
            except ValueError:
                # malformed attr
                pass
        return parsed
