# BedrockData
Blobs of data generated from Minecraft: Bedrock Edition used by PocketMine-MP

<table>
 <thead>
  <td>File</td>
  <td>Source</td>
  <td>Description</td>
  <td>Used for</td>
 </thead>
 <tbody>
  <tr>
   <td><code>banner_patterns.json</code></td>
   <td>Manually written</td>
   <td>All known banner pattern types and their crafting requirements. Not currently auto-generated.</td>
   <td>Not currently used</td>
  </tr>
  <tr>
   <td><code>biome_definitions.json</code></td>
   <td>Vanilla packet traces</td>
   <td>
    JSON representation of basic biome definitions obtained from <code>BiomeDefinitionListPacket</code>.<br/>
    Note that the client-side chunk generation data is <strong>not</strong> included.
   </td>
   <td>Populating <code>BiomeDefinitionListPacket</code> in a server</td>
  </tr>
  <tr>
   <td><code>biome_id_map.json</code></td>
   <td><a href="https://github.com/pmmp/bds-mod-mapping">BDS mod</a></td>
   <td>Mapping of Minecraft string biome IDs to their legacy integer ID counterparts</td>
   <td>Network serializing chunks</td>
  </tr>
  <tr>
   <td><code>block_id_to_item_id_map.json</code></td>
   <td><a href="https://github.com/pmmp/bds-mod-mapping">BDS mod</a></td>
   <td>
    Map of block string IDs to item IDs.<br/>
    Usually these are the same, but differ in a few cases such as for some doors.
   </td>
   <td>Saving blocks to disk in inventories</td>
  </tr>

  <tr>
   <td><code>block_properties_table.json</code></td>
   <td><a href="https://github.com/pmmp/bds-mod-mapping">BDS mod</a></td>
   <td>Basic data for all known block types, such as hardness, opacity etc</td>
   <td>Implementing new blocks & behaviour parity</td>
  </tr>

  <tr>
   <td><code>block_state_meta_map.json</code></td>
   <td><a href="https://github.com/pmmp/bds-mod-mapping">BDS mod</a></td>
   <td>List of meta values for each state ID in <code>canonical_block_states.nbt</code></td>
   <td>Populating <code>CraftingDataPacket</code></td>
  </tr>

  <tr>
   <td><code>canonical_block_states.nbt</code></td>
   <td><a href="https://github.com/pmmp/bds-mod-mapping">BDS mod</a></td>
   <td>
    List of `TAG_Compound` (in varint NBT format), one for each predefined blockstate.<br/>
    The network ID of a state is its position in the list.
   </td>
   <td>
    Network serializing block updates, chunks etc.
   </td>
  </tr>

  <tr>
   <td><code>command_arg_types.json</code></td>
   <td><a href="https://github.com/pmmp/bds-mod-mapping">BDS mod</a></td>
   <td>All known command arg types and identifiers</td>
   <td>Generating constants for <code>AvailableCommandsPacket</code></td>
  </tr>

  <tr>
   <td><code>entity_id_map.json</code></td>
   <td>Vanilla packet traces</td>
   <td>List of legacy numeric save IDs and their string counterparts</td>
   <td>Upgrading old entity save data</td>
  </tr>

  <tr>
   <td><code>entity_identifiers.nbt</code></td>
   <td>Vanilla packet traces</td>
   <td>Entity type definitions for <code>AvailableActorIdentifiersPacket</code></td>
   <td>Populating <code>AvailableActorIdentifiersPacket</code> in a server</td>
  </tr>

  <tr>
   <td><code>enums.py</code></td>
   <td>Manually written</td>
   <td>Script for scraping enum definitions from the <a href="https://github.com/Mojang/bedrock-protocol-docs">protocol spec</a></td>
   <td>Scraping enums for easier code generation data sources</td>
  </tr>

  <tr>
   <td><code>item_tags.json</code></td>
   <td><a href="https://github.com/pmmp/bds-mod-mapping">BDS mod</a></td>
   <td>All known item tags and the IDs they contain</td>
   <td>Parsing crafting recipes from <code>CraftingDataPacket</code></td>
  </tr>

  <tr>
   <td><code>level_sound_id_map.json</code></td>
   <td><a href="https://github.com/pmmp/bds-mod-mapping">BDS mod</a></td>
   <td>All known sound IDs for <code>LevelSoundEventPacket</code></td>
   <td>Generating constants for <code>LevelSoundEventPacket</code></td>
  </tr>

  <tr>
   <td><code>protocol_info.json</code></td>
   <td><a href="https://github.com/pmmp/bds-modding-devkit/blob/master/protocol_info_dumper.py">Binary analysis script</a></td>
   <td>Version info and packet ID list</td>
   <td>Generating barebones code for protocol updates</td>
  </tr>

  <tr>
   <td><code>r12_to_current_block_map.bin</code></td>
   <td><a href="https://github.com/pmmp/bds-mod-mapping">BDS mod</a></td>
   <td>Mapping of 1.12 block ID/meta to the current version's blockstate NBT</td></td>
   <td>No longer used as of PM5, slated for removal</td>
  </tr>

  <tr>
   <td><code>r16_to_current_item_map.json</code></td>
   <td><a href="https://github.com/pmmp/bds-mod-mapping">BDS mod</a></td>
   <td>Mappings for legacy item ID/meta to new IDs</td>
   <td>Generating schemas for <a href="https://github.com/pmmp/BedrockItemUpgradeSchema">BedrockItemUpgradeSchema</a></td>
  </tr>

  <tr>
   <td><code>required_item_list.json</code></td>
   <td>Vanilla packet traces</td>
   <td>Network dictionary of string item ID -> network ID</td>
   <td>Network serializing itemstacks</td>
  </tr>

  <tr>
   <td><code>creative/*.json</code></td>
   <td>Vanilla packet traces</td>
   <td>Creative inventory contents, split by tab</td>
   <td>Supporting creative inventory as a server</td>
  </tr>

  <tr>
   <td><code>enums/*json</code></td>
   <td>Scraped from <a href="https://github.com/Mojang/bedrock-protocol-docs">protocol spec</a></td>
   <td>Useful enum values</td>
   <td>Code generation</td>
  </tr>

  <tr>
   <td><code>recipes/*.json</code></td>
   <td>Vanilla packet traces</td>
   <td>Crafting, smelting, brewing recipe definitions</td>
   <td>Supporting crafting, smelting & brewing as a server</td>
  </tr>
 </tbody>
</table>
