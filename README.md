# Charm the Commuter: Forecast a City That Isn't

Entry for the [make.fun bounty](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
`u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e`.

## The entry

`main.py` writes a single line of weather forecast — at most 140
characters — for a city that does not exist, to `/output/entry.txt`:

> In Wobbleford, drizzle till nine, then bright sun — the 8:12 bus is on
> time, the pigeons applaud, and your umbrella gets a lie-in.

Wobbleford is invented. The line keeps the rhythm of a real broadcast
forecast, names the city and its weather, gives the place one concrete
detail (the applauding pigeons on the platform), and ends on a small joke
for the bored commuter at the bus stop: after a morning of drizzle, even
the umbrella gets a lie-in.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

No network, no input, no secrets. The program is deterministic: it always
writes the same line.
