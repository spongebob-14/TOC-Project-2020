# Assistant of Game "Sky: Children of the Light"

## QR code
![QR](./img/qr.png)

## Interface
![demo](./img/demo.jpg)

## Some main part of game
* make friend and collaborate with other players
* find spirit in realm and unlock the expressions (actions, voices, postures) 
* collecting candle as currency and trading costume

## Function that assistant help
* reference for the place of spirit
* reference for the place of candle

---------

## Setup

### Prerequisite
* Python 3.6
* Pipenv
* Facebook Page and App
* HTTPS Server

#### Install Dependency
```sh
pip3 install pipenv

pipenv --three

pipenv install

pipenv shell
```

* pygraphviz (For visualizing Finite State Machine)
    * [Setup pygraphviz on Ubuntu](http://www.jianshu.com/p/a3da7ecc5303)
	* [Note: macOS Install error](https://github.com/pygraphviz/pygraphviz/issues/100)


#### Secret Data
You should generate a `.env` file to set Environment Variables refer to our `.env.sample`.
`LINE_CHANNEL_SECRET` and `LINE_CHANNEL_ACCESS_TOKEN` **MUST** be set to proper values.
Otherwise, you might not be able to run your code.

#### Run the sever

```sh
python3 app.py
```

## Finite State Machine
![fsm](./img/fsm.png)

* two kind of questions, for candle or spirit
* in candle state, input the map name return the position of candles in that map
* in spirit stat, input the map name return the position of spirits in that map


## Usage
The initial state is set to `user`.

Every time `user` state is triggered to `advance` to another state, it will `go_back` to `user` state after the bot replies corresponding message.

* user
	* Input: "go to state1"
		* Reply: "I'm entering state1"

	* Input: "go to state2"
		* Reply: "I'm entering state2"
