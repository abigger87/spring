# Spring

Oasis ERC721 Cairo Contracts

Deploy `/contracts/tokens/ERC721.cairo` to StarkNet to have the NFTs available for trading on [Oasis](https://playoasis.xyz/). Please see the [Cairo documentation](https://www.cairo-lang.org/docs/) for more information on deploying contracts.

## Setup env

```
python3 -m venv env
source env/bin/activate
pip install git+https://github.com/OpenZeppelin/nile.git
nile install
```

## Create a Starknet Account

On Testnet:
```sh
export STARKNET_WALLET=starkware.starknet.wallets.open_zeppelin.OpenZeppelinAccount
starknet deploy_account --network alpha-goerli
```

On Mainnet:
```sh
export STARKNET_WALLET=starkware.starknet.wallets.open_zeppelin.OpenZeppelinAccount
starknet deploy_account --network alpha-mainnet
```

## Compiling/Building

```sh
nile compile

# OR

starknet-compile contracts/token/ERC721.cairo \
    --output artifacts/ERC721.json \
    --abi artifacts/abis/ERC721.json
```

## Deploying

Set the Starknet Network environment variable to use the starknet testnet.

```sh
export STARKNET_NETWORK=alpha-goerli
```

Deploy the compiled ERC721 contract to the network.

```sh
nile deploy ERC721 --alias ERC721 9711010011410197115  9710898 0x05939883bfbb4940e9294a9c0835d83f56b83d1e73a48e9cc94f35e3dec3ad4c 1 0x10 --network=alpha-goerli
# OR
starknet deploy --contract artifacts/ERC721.json --inputs 9711010011410197115 9710898 0x05939883bfbb4940e9294a9c0835d83f56b83d1e73a48e9cc94f35e3dec3ad4c 1 0x10 --gateway_url=https://alpha4.starknet.io
```

Note: At the time of writing, the Alpha Goerli Testnet gateway url is `https://alpha4.starknet.io`.
Mainnet is `https://alpha-mainnet.starknet.io`.

Reference the [cairo docs](https://www.cairo-lang.org/docs/hello_starknet/index.html#starknet-alpha-version-4-on-goerli) to view up-to-date deployment information.

Expected output should be similar to:

```sh
Deploy transaction was sent.
Contract address: 0x03e1205a1ac98c43313adaca25705c21bf6bd5201f13f303e8bb5e64992e0ae3
Transaction hash: 0x7057186b08a924dab706a0282029743eb214a34bb071b1e954b8c075d226de1
```

The contract can be viewed on the testnet explorer: [https://goerli.voyager.online/](https://goerli.voyager.online/contract/0x03e1205a1ac98c43313adaca25705c21bf6bd5201f13f303e8bb5e64992e0ae3)

Verify your contract on Voyager's verify [page](https://goerli.voyager.online/verifyContract).

## Deploying an encoded uri

To encode your uri, enter the [utils](./utils) directory and change the text string to your url.

Then run
```sh
python3 translate_uri.py
```

You should get an output like:
```sh
Deploy transaction was sent.
Contract address: 0x04937fcd848f24d853eacefc0c4f2516b36215b8aa0b6bc7c72ca94fcd57576b
Transaction hash: 0x7c419ad22f34e82a45e19c30fe43c70cc80690e8f8055c674ebf087f4bcd338
```

Then deploy the ERC721 with those arguments as the last 2 arguments.
```sh
starknet deploy --contract artifacts/ERC721.json --inputs 9711010011410197115 9710898 0x05939883bfbb4940e9294a9c0835d83f56b83d1e73a48e9cc94f35e3dec3ad4c 5 184555836509371486644779699072878786229410346258767650844634294430945521251 196873592451930689838827194581964303318756410344301147590634314104740210296 101237978808539379729471660198892962658853636293393561363721320487753958767 186127600646926679413315537543401666819700210029644436125161208314875835749 6687128967121684679280371266352 --gateway_url=https://alpha4.starknet.io
```


## Need help?

Reference the original Oasis Contracts [GitHub Repository](https://github.com/playoasis/starknet-contracts).

## Acknowledgements

These contracts were inspired by or directly modified from many sources, primarily:

- [OpenZeppelin](https://github.com/OpenZeppelin/cairo-contracts)

