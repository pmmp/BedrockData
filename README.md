# BedrockData
Blobs of JSON data generated from Minecraft: Bedrock Edition used by PocketMine-MP

### `required_block_states.json`
This file contains data defining all the needed block states in MCPE's StartGamePacket. The format is as follows:
<details><summary>Show</summary>
<pre>
"prefix": {
   "block_id": [
       /* all of the needed metadata variants (or states in the future) */
       0,
       1,
       2,
       3
   ]
}
</pre>
</details>

### `block_id_map.json`
This file contains a mapping of all block stringy IDs to legacy numeric IDs (which are still used internally, and still needed by third party developers for conversion and for items).

#### Note
Where a block's legacy ID is > 255, its item ID is `255 - legacyBlockId`. This means prismarine stairs = -2 and so on.

### `item_id_map.json`
This file contains a mapping of all item stringy IDs to legacy numeric IDs.

### `banner_patterns.json`
This file defines all the known banner pattern types and their crafting requirements.

### `recipes.json`
This file defines all crafting-table, furnace and chemistry recipes. This includes recipes for the smoker, cartography table etc.

#### Note
Brewing recipes are **not** included because Mojang don't see fit to send these over network.

### `creativeitems.json`
This file contains an ordered list of items which appear in the vanilla creative inventory with Education Edition and Experimental Gameplay enabled.
