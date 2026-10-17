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
| [description](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/description/) | val [description](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/description/): [String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html)<br>[String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html) description - A description of the pack, that shortly describes what the pack does |
| [GSON](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/g-s-o-n/) | val [GSON](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/g-s-o-n/): Gson<br>Gson GSON - Writes json objects to json files |
| [name](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/name/) | val [name](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/name/): [String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html)<br>[String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html) name - The name of the pack that gets generated |
| [packFormat](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/pack-format/) | val [packFormat](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/pack-format/): PackFormat.IntermediaryFormat<br>PackFormat.IntermediaryFormat packFormat - The format this pack was developed for. |

## Functions

| Name | Summary |
|---|---|
| [getPath](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/get-path/) | open fun [getPath](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/get-path/)(): [Path](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/nio/file/Path.html) |
| [write](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/write/) | abstract fun [write](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/write/)()<br>A method that writes **all** data to disk. |
| [writeMetadata](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/write-metadata/) | open fun [writeMetadata](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/write-metadata/)()<br>This method is used for writing the pack.mcmeta file characterising the pack. |
| [writePackIcon](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/write-pack-icon/) | open fun [writePackIcon](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/write-pack-icon/)(modId: [String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html))<br>An optional method that does not need to be called, but exists to give authors an option to customise their pack. |
