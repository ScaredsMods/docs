---
title: "AdvancedInfuserBlockEntity"
sidebar:
  label: "Overview"
---

```kotlin
open class AdvancedInfuserBlockEntity : AbstractTickingBlockEntity
```

## Constructors

| | |
|---|---|
| [AdvancedInfuserBlockEntity](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/advanced-infuser-block-entity/) | constructor(pos: BlockPos, blockState: BlockState) |

## Properties

| Name | Summary |
|---|---|
| [BOTTLE_OUTPUT_SLOT](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/b-o-t-t-l-e_-o-u-t-p-u-t_-s-l-o-t/) | val [BOTTLE_OUTPUT_SLOT](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/b-o-t-t-l-e_-o-u-t-p-u-t_-s-l-o-t/): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = 3 |
| [INFUSED_TOTEM_INPUT_SLOT](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/i-n-f-u-s-e-d_-t-o-t-e-m_-i-n-p-u-t_-s-l-o-t/) | val [INFUSED_TOTEM_INPUT_SLOT](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/i-n-f-u-s-e-d_-t-o-t-e-m_-i-n-p-u-t_-s-l-o-t/): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = 0 |
| [INFUSED_TOTEM_OUTPUT_SLOT](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/i-n-f-u-s-e-d_-t-o-t-e-m_-o-u-t-p-u-t_-s-l-o-t/) | val [INFUSED_TOTEM_OUTPUT_SLOT](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/i-n-f-u-s-e-d_-t-o-t-e-m_-o-u-t-p-u-t_-s-l-o-t/): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = 2 |
| [POTION_INPUT_SLOT](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/p-o-t-i-o-n_-i-n-p-u-t_-s-l-o-t/) | val [POTION_INPUT_SLOT](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/p-o-t-i-o-n_-i-n-p-u-t_-s-l-o-t/): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = 1 |
| [stackHandler](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/stack-handler/) | val [stackHandler](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/stack-handler/): ItemStacksResourceHandler |

## Functions

| Name | Summary |
|---|---|
| [craftItem](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/craft-item/) | open fun [craftItem](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/craft-item/)() |
| [createMenu](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/create-menu/) | @Nullable<br>open fun [createMenu](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/create-menu/)(containerId: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html), playerInventory: Inventory, player: Player): @NullableAbstractContainerMenu |
| [drops](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/drops/) | open fun [drops](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/drops/)() |
| [getUpdatePacket](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/get-update-packet/) | @Nullable<br>open fun [getUpdatePacket](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/get-update-packet/)(): @NullablePacket&lt;ClientGamePacketListener&gt; |
| [getUpdateTag](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/get-update-tag/) | open fun [getUpdateTag](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/get-update-tag/)(registries: HolderLookup.Provider): CompoundTag |
| [hasCraftingFinished](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/has-crafting-finished/) | open fun [hasCraftingFinished](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/has-crafting-finished/)(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) |
| [hasRecipe](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/has-recipe/) | open fun [hasRecipe](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/has-recipe/)(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) |
| [increaseCraftingProgress](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/increase-crafting-progress/) | open fun [increaseCraftingProgress](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/increase-crafting-progress/)() |
| [isOutputSlotEmptyOrReceivable](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/is-output-slot-empty-or-receivable/) | open fun [isOutputSlotEmptyOrReceivable](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/is-output-slot-empty-or-receivable/)(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) |
| [loadAdditional](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/load-additional/) | open fun [loadAdditional](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/load-additional/)(input: ValueInput) |
| [onDataPacket](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/on-data-packet/) | open fun [onDataPacket](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/on-data-packet/)(net: Connection, valueInput: ValueInput) |
| [preRemoveSideEffects](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/pre-remove-side-effects/) | open fun [preRemoveSideEffects](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/pre-remove-side-effects/)(pos: BlockPos, state: BlockState) |
| [resetProgress](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/reset-progress/) | open fun [resetProgress](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/reset-progress/)() |
| [saveAdditional](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/save-additional/) | open fun [saveAdditional](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/save-additional/)(output: ValueOutput) |
| [setChanged](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/set-changed/) | open fun [setChanged](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/set-changed/)() |
| [tick](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/tick/) | open fun [tick](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/tick/)(level: Level, blockPos: BlockPos, blockState: BlockState) |
