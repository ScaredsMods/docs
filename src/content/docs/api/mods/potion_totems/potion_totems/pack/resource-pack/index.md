---
title: "ResourcePack"
sidebar:
  label: "Overview"
---

```kotlin
open class ResourcePack : AbstractPack
```

## Constructors

| | |
|---|---|
| [ResourcePack](/docs/api/mods/potion_totems/potion_totems/pack/resource-pack/resource-pack/) | constructor(name: [String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html), description: [String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html), packFormat: PackFormat.IntermediaryFormat) |

## Types

| Name | Summary |
|---|---|
| [TranslationModule](/docs/api/mods/potion_totems/potion_totems/pack/resource-pack/translation-module/) | open class [TranslationModule](/docs/api/mods/potion_totems/potion_totems/pack/resource-pack/translation-module/) |

## Functions

| Name | Summary |
|---|---|
| [apply](/docs/api/mods/potion_totems/potion_totems/pack/resource-pack/apply/) | open fun [apply](/docs/api/mods/potion_totems/potion_totems/pack/resource-pack/apply/)()<br>A method that must be called if you want to actually use the resources generated. |
| [getTranslationModule](/docs/api/mods/potion_totems/potion_totems/pack/resource-pack/get-translation-module/) | open fun [getTranslationModule](/docs/api/mods/potion_totems/potion_totems/pack/resource-pack/get-translation-module/)(): [ResourcePack.TranslationModule](/docs/api/mods/potion_totems/potion_totems/pack/resource-pack/translation-module/) |
| [write](/docs/api/mods/potion_totems/potion_totems/pack/resource-pack/write/) | open fun [write](/docs/api/mods/potion_totems/potion_totems/pack/resource-pack/write/)()<br>An example implementation of [write](/docs/api/mods/potion_totems/potion_totems/pack/abstract-pack/write/), used for resourcepacks. |
