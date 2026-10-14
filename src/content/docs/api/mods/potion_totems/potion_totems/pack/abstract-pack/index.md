---
title: "AbstractPack"
sidebar:
  label: "Overview"
---

abstract class [AbstractPack](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/)

#### Inheritors

| |
|---|
| [DataPack](/docs/api/mods/potion_totems/potion_totems/pack/data-pack/) |
| [ResourcePack](/docs/api/mods/potion_totems/potion_totems/pack/resource-pack/) |

## Constructors

| | |
|---|---|
| [AbstractPack](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/abstract-pack/) | constructor(name: [String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html), description: [String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html), type: [AbstractPack.PackType](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/pack-type/), packFormat: PackFormat.IntermediaryFormat) |

## Types

| Name | Summary |
|---|---|
| [PackType](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/pack-type/) | enum [PackType](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/pack-type/) |

## Properties

| Name | Summary |
|---|---|
| [description](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/description/) | val [description](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/description/): [String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html) |
| [GSON](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/g-s-o-n/) | val [GSON](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/g-s-o-n/): Gson |
| [name](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/name/) | val [name](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/name/): [String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html)<br>[String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html) name - The name of the pack that get's generated [String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html) description - A description of the pack, that shortly describes what the pack does [PackType](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/pack-type/) packType - What type of pack this is: Resource or datapack PackFormat.IntermediaryFormat packFormat - The format this pack was developed for. |
| [packFormat](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/pack-format/) | val [packFormat](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/pack-format/): PackFormat.IntermediaryFormat |

## Functions

| Name | Summary |
|---|---|
| [getPath](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/get-path/) | open fun [getPath](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/get-path/)(): [Path](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/nio/file/Path.html) |
| [write](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/write/) | abstract fun [write](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/write/)() |
| [writeMetadata](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/write-metadata/) | open fun [writeMetadata](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/write-metadata/)() |
| [writePackIcon](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/write-pack-icon/) | open fun [writePackIcon](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/write-pack-icon/)(modId: [String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html)) |
