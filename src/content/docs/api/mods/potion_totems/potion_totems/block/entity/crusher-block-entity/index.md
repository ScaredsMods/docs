---
title: "CrusherBlockEntity"
sidebar:
  label: "Overview"
---

```kotlin
open class CrusherBlockEntity : AbstractTickingBlockEntity
```

## Constructors

| | |
|---|---|
| [CrusherBlockEntity](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/crusher-block-entity/) | constructor(pos: BlockPos, state: BlockState) |

## Properties

| Name | Summary |
|---|---|
| [INPUT_SLOT](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/i-n-p-u-t_-s-l-o-t/) | val [INPUT_SLOT](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/i-n-p-u-t_-s-l-o-t/): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = 0 |
| [OUTPUT_SLOT_1](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/o-u-t-p-u-t_-s-l-o-t_1/) | val [OUTPUT_SLOT_1](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/o-u-t-p-u-t_-s-l-o-t_1/): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = 1 |
| [OUTPUT_SLOT_2](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/o-u-t-p-u-t_-s-l-o-t_2/) | val [OUTPUT_SLOT_2](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/o-u-t-p-u-t_-s-l-o-t_2/): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = 2 |
| [OUTPUT_SLOT_3](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/o-u-t-p-u-t_-s-l-o-t_3/) | val [OUTPUT_SLOT_3](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/o-u-t-p-u-t_-s-l-o-t_3/): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = 3 |
| [OUTPUT_SLOT_4](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/o-u-t-p-u-t_-s-l-o-t_4/) | val [OUTPUT_SLOT_4](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/o-u-t-p-u-t_-s-l-o-t_4/): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = 4 |
| [OUTPUT_SLOT_5](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/o-u-t-p-u-t_-s-l-o-t_5/) | val [OUTPUT_SLOT_5](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/o-u-t-p-u-t_-s-l-o-t_5/): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = 5 |
| [OUTPUT_SLOT_6](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/o-u-t-p-u-t_-s-l-o-t_6/) | val [OUTPUT_SLOT_6](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/o-u-t-p-u-t_-s-l-o-t_6/): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = 6 |
| [OUTPUT_SLOT_7](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/o-u-t-p-u-t_-s-l-o-t_7/) | val [OUTPUT_SLOT_7](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/o-u-t-p-u-t_-s-l-o-t_7/): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = 7 |
| [OUTPUT_SLOT_8](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/o-u-t-p-u-t_-s-l-o-t_8/) | val [OUTPUT_SLOT_8](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/o-u-t-p-u-t_-s-l-o-t_8/): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = 8 |
| [OUTPUT_SLOT_9](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/o-u-t-p-u-t_-s-l-o-t_9/) | val [OUTPUT_SLOT_9](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/o-u-t-p-u-t_-s-l-o-t_9/): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = 9 |
| [resourceHandler](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/resource-handler/) | val [resourceHandler](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/resource-handler/): ItemStacksResourceHandler |

## Functions

| Name | Summary |
|---|---|
| [craftItem](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/craft-item/) | open fun [craftItem](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/craft-item/)() |
| [createMenu](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/create-menu/) | @Nullable<br>open fun [createMenu](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/create-menu/)(pContainerId: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html), pPlayerInventory: Inventory, pPlayer: Player): @NullableAbstractContainerMenu |
| [drops](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/drops/) | open fun [drops](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/drops/)() |
| [getCurrentRecipe](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/get-current-recipe/) | open fun [getCurrentRecipe](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/get-current-recipe/)(): [Optional](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html)&lt;RecipeHolder&lt;[CrusherRecipe](/docs/api/mods/potion_totems/potion_totems/recipe/crusher-recipe/)&gt;&gt; |
| [getDisplayName](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/get-display-name/) | open fun [getDisplayName](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/get-display-name/)(): Component |
| [hasCraftingFinished](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/has-crafting-finished/) | open fun [hasCraftingFinished](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/has-crafting-finished/)(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) |
| [hasRecipe](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/has-recipe/) | open fun [hasRecipe](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/has-recipe/)(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) |
| [increaseCraftingProgress](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/increase-crafting-progress/) | open fun [increaseCraftingProgress](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/increase-crafting-progress/)() |
| [isOutputSlotEmptyOrReceivable](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/is-output-slot-empty-or-receivable/) | open fun [isOutputSlotEmptyOrReceivable](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/is-output-slot-empty-or-receivable/)(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) |
| [resetProgress](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/reset-progress/) | open fun [resetProgress](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/reset-progress/)() |
| [tick](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/tick/) | open fun [tick](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/tick/)(level: Level, pPos: BlockPos, pState: BlockState) |
