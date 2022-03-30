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

## Authors
We are students at HSE masters program "Computational Linguistics":
- Nata Kiseleva
- Daniil Larionov (corresponding author: dslarionov@edu.hse.ru)
- Liliya Kazakova
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Cite
Consider citing us if you find our work useful

```
@unpublished{
  larionov_kiseleva_kazakova_kudrinski_cherepanova,
  place={Higher School of Economics, Moscow, Russia},
  title={Named Entity Recognition in Dialogues},
  url={https://docs.google.com/document/d/1tviLZe8XKdRGKkOdNS-1I7oPt3okD6VPAHB1Cz94nx8/edit},
  journal={Google Docs},
  author={Larionov, Danil and Kiseleva, Natalia and Kazakova, Liliya and Kudrinski, Maxime and Cherepanova, Olga}
} 
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
