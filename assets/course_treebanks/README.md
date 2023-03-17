# ParallelTreebank-FinalProject
## The Source of Sentences

The 50 sentences presented in this treebank are a selection of the Tatoeba (https://tatoeba.org/en/) public database. The two reference databases for "Sentences" and "Original and Translated Sentences" (https://tatoeba.org/en/downloads) were downloaded and cross-referenced to identify those records for which at least one translation was provided for all of the languages of this treebank. After identifying sentences that met this condition, our team performed a hand-picked selection, favoring sentences higher in token length and those with uncommon structures. 

In the resulting treebank, all sentences carry a reference to the original Tatoeba Sentence Id for future reference or research. For non-english translations, both the Sentence Id of the translation and of the English version is provided, as well as the text of the sentence in English. 

All annotations are validated by the [UD validation tool.](https://github.com/UniversalDependencies/tools)

### Simplified Chinese (by Xiao Wang)
#### Not included in (thus unrecognized by) the validation tool
- 应该(should), 要(be going to), 会(will/would) and 能(can/could), 不会 and 不能 are not recognized as model verbs in validation.
- 是(be) and 不是, 就是, 也是, 都是 are all not recognized as copula in validation. And according to UD, even though 是 is often used as copula but its POS is VERB not AUX which also causes error in validation (because it doesn't allow verb to be with aux relation, only aux can be in aux relation.)
- Because of the relation ***nsubj:pass***, the validation complains about the sentence has two subjects (nsubj:pass and nsubj).

#### Language specific UD relations and features
- Relation ***compound:ext*** for 得,  [see examples here.](https://universaldependencies.org/treebanks/zh_gsdsimp/zh_gsdsimp-dep-compound-ext.html)
- Relation ***acl:relcl*** and ***mark:rel*** for 的, [see examples here, ](https://universaldependencies.org/treebanks/zh_gsdsimp/zh_gsdsimp-dep-acl-relcl.html)
in contract to the generative 的, [see the first example on this link](https://universaldependencies.org/treebanks/zh_gsdsimp/zh_gsdsimp-dep-case.html).
- Relation ***obl:patient*** for the relation between the noun and verb in "将/把 + NOUN + VERB" structure, [see examples here.](https://universaldependencies.org/treebanks/zh_gsdsimp/zh_gsdsimp-dep-obl-patient.html)
- Relation ***aux:pass*** for verb 被 in passive voice, [see examples here.](https://universaldependencies.org/treebanks/zh_gsdsimp/zh_gsdsimp-dep-nsubj-pass.html) It's debatable if 被 should be VERB or other POS.
- Relation ***nsubj:pass*** for nouns (actually patient) before 被 or 为(...所), [see examples from ***aux:pass***](https://universaldependencies.org/treebanks/zh_gsdsimp/zh_gsdsimp-dep-nsubj-pass.html).
- Relation ***mark:adv*** for 的 and 地 before verb, [see examples here.](https://universaldependencies.org/treebanks/zh_gsdsimp/zh_gsdsimp-dep-mark-adv.html)
- Feature ***Aspect=Perf*** for aux 过 and 了 after verbs.
- Relation ***discourse*** for 了 and 的 in the end of a sentence as particles.
- Relation ***discourse:sp*** for particles 吗, 呢, 吧, [see examples here.](https://universaldependencies.org/treebanks/zh_gsdsimp/zh_gsdsimp-dep-discourse-sp.html)
- Relation ***clf*** for classifiers, [see examples here.](https://universaldependencies.org/treebanks/zh_gsdsimp/zh_gsdsimp-dep-clf.html)


### German (by Nino)
- `wirst` is not recognized aus auxiliary verb bei the UD validation tool (however, it still is one and annotated as such in other UD treebanks)

### English (by Qin Gu)
- Validation passed.

### Hungarian (by Aron)
- Punctuation was omitted from the annotation, resulting in validation errors
- `Value 2 of feature Person[psor] is not permitted with UPOS NOUN in language [hu]` is reported as a validation error; despite this, we have very high confidence in the annotation that caused the error
- `volna` is reported as not being an auxiliary in Hungarian by the validation tool - however, this is the common analysis in other reviewed treebanks
