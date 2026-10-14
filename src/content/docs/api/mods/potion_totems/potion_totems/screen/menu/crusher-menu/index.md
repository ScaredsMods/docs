---
title: "CrusherMenu"
sidebar:
  label: "Overview"
---

```kotlin
open class CrusherMenu : AbstractContainerMenu
```

## Constructors

| | |
|---|---|
| [CrusherMenu](/docs/api/mods/potion_totems/potion_totems/screen/menu/crusher-menu/crusher-menu/) | constructor(containerId: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html), inv: Inventory, buf: FriendlyByteBuf)constructor(containerId: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html), inv: Inventory, blockEntity: BlockEntity, resourceHandler: ItemStacksResourceHandler, data: ContainerData) |

## Properties

| Name | Summary |
|---|---|
| [blockEntity](/docs/api/mods/potion_totems/potion_totems/screen/menu/crusher-menu/block-entity/) | val [blockEntity](/docs/api/mods/potion_totems/potion_totems/screen/menu/crusher-menu/block-entity/): [CrusherBlockEntity](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/) |

## Functions

| Name | Summary |
|---|---|
| [getScaledArrowProgress](/docs/api/mods/potion_totems/potion_totems/screen/menu/crusher-menu/get-scaled-arrow-progress/) | open fun [getScaledArrowProgress](/docs/api/mods/potion_totems/potion_totems/screen/menu/crusher-menu/get-scaled-arrow-progress/)(): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |
| [isCrafting](/docs/api/mods/potion_totems/potion_totems/screen/menu/crusher-menu/is-crafting/) | open fun [isCrafting](/docs/api/mods/potion_totems/potion_totems/screen/menu/crusher-menu/is-crafting/)(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) |
| [quickMoveStack](/docs/api/mods/potion_totems/potion_totems/screen/menu/crusher-menu/quick-move-stack/) | open fun [quickMoveStack](/docs/api/mods/potion_totems/potion_totems/screen/menu/crusher-menu/quick-move-stack/)(playerIn: Player, pIndex: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)): ItemStack |
| [stillValid](/docs/api/mods/potion_totems/potion_totems/screen/menu/crusher-menu/still-valid/) | open fun [stillValid](/docs/api/mods/potion_totems/potion_totems/screen/menu/crusher-menu/still-valid/)(player: Player): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) |
