# BedrockData
Blobs of data generated from Minecraft: Bedrock Edition used by PocketMine-MP

## canonical_block_states.nbt
This file contains an ordered list of `TAG_Compound`s (in varint NBT format) representing the pre-agreed blockstates in MCPE.
The runtime ID of a state is the offset in the list that the state appears.
The contents of this file are extracted from the vanilla BDS using [`pmmp/mapping`](https://github.com/pmmp/mapping).

## block_state_meta_map.json
This file contains a mapping of all blockstate IDs (as per `canonical_block_states.nbt`) to their associated internal meta values.
The position in the list is the blockstate ID, and the value is the blockstate's associated meta value.
This information is used for interpreting and serializing crafting recipes on the network in PM5.

Note: While the values may **appear** to be contiguous, they are not - in some cases there are holes. This means that you can't always get away with just assigning an increasing integer to each blockstate as its meta value.

## banner_patterns.json
This file defines all the known banner pattern types and their crafting requirements.

## recipes.json
This file defines all crafting-table, furnace and chemistry recipes. This includes recipes for the smoker, cartography table etc.

## creativeitems.json
This file contains an ordered list of items which appear in the vanilla creative inventory with Education Edition and Experimental Gameplay enabled.

## biome_definitions.nbt
This file contains a network-format NBT blob containing biome definitions obtained from `BiomeDefinitionListPacket`.

## biome_id_map.json
This file contains a mapping of Minecraft string biome IDs to their legacy integer ID counterparts. While biome IDs aren't dynamic yet, it's expected they will become dynamic in the future.

## entity_identifiers.nbt
This file contains a network-format NBT blob containing entity identifier mappings obtained from `AvailableActorIdentifiersPacket`.

## level_sound_id_map.json
This file contains a mapping of string sound names to LevelSoundEvent IDs used by LevelSoundEventPacket.

Note that this file may be missing some IDs (it is generated from vanilla using [pmmp/mapping](https://github.com/pmmp/mapping), and vanilla itself is missing some mappings).

## enums.py
This file contains a python script which scrapes enums from [Mojang/bedrock-protocol/docs](https://github.com/Mojang/bedrock-protocol-docs) to generate JSON files in the `enums` directory which can be used by other tools.
 - ParticleType
