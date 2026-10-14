---
title: "ModModelProvider"
sidebar:
  label: "Overview"
---

```kotlin
open class ModModelProvider : ModelProvider
```

## Constructors

| | |
|---|---|
| [ModModelProvider](/docs/api/mods/potion_totems/potion_totems/datagen/mod-model-provider/mod-model-provider/) | constructor(output: PackOutput) |

## Functions

| Name | Summary |
|---|---|
| [createFlatItemModel](/docs/api/mods/potion_totems/potion_totems/datagen/mod-model-provider/create-flat-item-model/) | open fun [createFlatItemModel](/docs/api/mods/potion_totems/potion_totems/datagen/mod-model-provider/create-flat-item-model/)(item: Item, suffix: [String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html), texture: Material, generators: ItemModelGenerators): Identifier |
| [createLayeredItemModel](/docs/api/mods/potion_totems/potion_totems/datagen/mod-model-provider/create-layered-item-model/) | open fun [createLayeredItemModel](/docs/api/mods/potion_totems/potion_totems/datagen/mod-model-provider/create-layered-item-model/)(item: Item, suffix: [String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html), layer0: Material, layer1: Material, generators: ItemModelGenerators): Identifier |
