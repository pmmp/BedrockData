# BedrockData
Blobs of data generated from Minecraft: Bedrock Edition used by PocketMine-MP

### `required_block_states.nbt`
This file contains a network-format NBT list of all the blockstate permutations needed by MCPE's `StartGamePacket`.
It's provided as-is directly from `StartGamePacket` sent by the current vanilla server.

### `block_id_map.json`
This file contains a mapping of all block stringy IDs to legacy numeric IDs (which are still used internally, and still needed by third party developers for conversion and for items).

#### Note
Where a block's legacy ID is > 255, its item ID is `255 - legacyBlockId`. This means prismarine stairs = -2 and so on.

### `r12_to_current_block_map.nbt`
This file contains a list of mappings from legacy pre-1.13 blockstates to states of the current version.
This data is obtained by plugging the legacy states into `BlockPalette` in the vanilla BDS using a mod, and writing the resulting NBT state obtained.
<details><summary>Schema</summary>

```
TAG_List: value={
   TAG_Compound: value={
      "old" => TAG_Compound: value={
         "name" => TAG_String: value="minecraft:example" //legacy string ID pre-1.13
         "val" => TAG_Short: value=0 //legacy block metadata pre-1.13
      }
      "new" => TAG_Compound: value={
         "name" => TAG_String: value="minecraft:new_example" //this might be different to the legacy ID in future versions!
         "states" => TAG_Compound: value={
            //list states here
         }
      }
   }
}
```

</details>

### `item_id_map.json`
This file contains a mapping of all item stringy IDs to legacy numeric IDs.

### `banner_patterns.json`
This file defines all the known banner pattern types and their crafting requirements.

### `recipes.json`
This file defines all crafting-table, furnace and chemistry recipes. This includes recipes for the smoker, cartography table etc.

### `creativeitems.json`
This file contains an ordered list of items which appear in the vanilla creative inventory with Education Edition and Experimental Gameplay enabled.

### `biome_definitions.nbt`
This file contains a network-format NBT blob containing biome definitions obtained from `BiomeDefinitionListPacket`.

### `entity_identifiers.nbt`
This file contains a network-format NBT blob containing entity identifier mappings obtained from `AvailableActorIdentifiersPacket`.
