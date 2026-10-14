---
title: "AdvancedInfuserMenu"
sidebar:
  label: "Overview"
---

```kotlin
open class AdvancedInfuserMenu : AbstractContainerMenu
```

## Constructors

| | |
|---|---|
| [AdvancedInfuserMenu](/docs/api/mods/potion_totems/potion_totems/screen/menu/advanced-infuser-menu/advanced-infuser-menu/) | constructor(containerId: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html), pInv: Inventory, extraData: FriendlyByteBuf)constructor(containerId: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html), pInv: Inventory, entity: BlockEntity, data: ContainerData) |

## Properties

| Name | Summary |
|---|---|
| [blockEntity](/docs/api/mods/potion_totems/potion_totems/screen/menu/advanced-infuser-menu/block-entity/) | val [blockEntity](/docs/api/mods/potion_totems/potion_totems/screen/menu/advanced-infuser-menu/block-entity/): [AdvancedInfuserBlockEntity](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/) |

## Functions

| Name | Summary |
|---|---|
| [getScaledArrowProgress](/docs/api/mods/potion_totems/potion_totems/screen/menu/advanced-infuser-menu/get-scaled-arrow-progress/) | open fun [getScaledArrowProgress](/docs/api/mods/potion_totems/potion_totems/screen/menu/advanced-infuser-menu/get-scaled-arrow-progress/)(): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |
| [isCrafting](/docs/api/mods/potion_totems/potion_totems/screen/menu/advanced-infuser-menu/is-crafting/) | open fun [isCrafting](/docs/api/mods/potion_totems/potion_totems/screen/menu/advanced-infuser-menu/is-crafting/)(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) |
| [quickMoveStack](/docs/api/mods/potion_totems/potion_totems/screen/menu/advanced-infuser-menu/quick-move-stack/) | open fun [quickMoveStack](/docs/api/mods/potion_totems/potion_totems/screen/menu/advanced-infuser-menu/quick-move-stack/)(playerIn: Player, pIndex: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)): ItemStack |
| [stillValid](/docs/api/mods/potion_totems/potion_totems/screen/menu/advanced-infuser-menu/still-valid/) | open fun [stillValid](/docs/api/mods/potion_totems/potion_totems/screen/menu/advanced-infuser-menu/still-valid/)(pPlayer: Player): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) |
