# NER Dialogues
The NER Dialogues project was created to train a chatbot to extract named entities from user queries. The developed model can extract book titles, movie titles, names of singers and composers, and song titles from short queries in Russian.

### Research Basis

See paper [here](https://docs.google.com/document/d/1tviLZe8XKdRGKkOdNS-1I7oPt3okD6VPAHB1Cz94nx8/edit).
## How to use

```python
from flair.models import SequenceTagger
from flair.data import Sentence

model: SequenceTagger = SequenceTagger.load("./final_model.pt")

example: Sentence = Sentence("Врубай Рамштайн!")
model.predict(example)

print(example.to_tagged_string())
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
