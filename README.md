# sportmonks-py
Python Package for SportsMonks API

Full details on the SportMonks API can be found [here](https://docs.sportmonks.com/football/) 

### Football

V3 of the SportMonks API is split into defined `Entities`, as listed below

- Fixture
- League, Season, Schedule, Stage and Round
- Team, Player, Squad, Coach and Referee
- Statistic
- Expected
- Standing and Topscorer
- Odd and Prediction
- Other

SportMonks imposes rate limits per entity (3000 per hour), hence this package separates endpoints by entity. More information
on entity rate limits can be viewed in the SportMonks documentation [here](https://docs.sportmonks.com/football/api/rate-limit).

For brevity and ease of use, entities have been mapped to a shortened keyword as below

| Entity Name | API Endpoint |
| ------------|--------------|
| Fixture     | fixture      |
 |League, Season, Schedule, Stage and Round | leagues      |
 | Team, Player, Squad, Coach and Referee | teams        |
| Statistic | statistics   |
| Expected | expected     |
| Standing and Topscorer | standings    |
| Odd and Prediction | odds         |
| Other | misc         |

### Documentation
Full documentation can be found at [ReadTheDocs](https://sportmonks-py.readthedocs.io/en/stable/)

### Installation

```bash
pip install sportmonks-py
```


#### Examples

See the `examples` directory for more examples on how to use the package.

### Returns
Given the size of the potential responses all calls return a generator object. This allows for the handling of large responses without the need to load the entire response into memory. The generator object can be iterated over to get the full response. The generators are defined depending on whether the call was asynchronous or not:
```python
StdResponse = Iterable[Iterator[dict[str, Any]]]
```
A standard (non-async) response is an iterable of iterators of dictionaries. The dictionaries contain the response data. The response data is paginated, so the iterators are used to iterate over the pages of data. 
```python
AsyncResponse = AsyncIterator[Iterator[dict[str, Any]]]
```
An async response is an async iterable of dictionaries. The dictionaries contain the response data. The response data is paginated, so the async iterable is used to iterate over the pages of data.

See the examples below for more information on how to use the response objects.
