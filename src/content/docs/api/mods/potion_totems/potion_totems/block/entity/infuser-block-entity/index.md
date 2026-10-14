---
title: "InfuserBlockEntity"
sidebar:
  label: "Overview"
---

```kotlin
open class InfuserBlockEntity : AbstractTickingBlockEntity
```

## Constructors

| | |
|---|---|
| [InfuserBlockEntity](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/infuser-block-entity/) | constructor(pos: BlockPos, state: BlockState) |

## Properties

| Name | Summary |
|---|---|
| [INPUT_SLOT_1](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/i-n-p-u-t_-s-l-o-t_1/) | val [INPUT_SLOT_1](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/i-n-p-u-t_-s-l-o-t_1/): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = 0 |
| [INPUT_SLOT_2](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/i-n-p-u-t_-s-l-o-t_2/) | val [INPUT_SLOT_2](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/i-n-p-u-t_-s-l-o-t_2/): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = 1 |
| [INPUT_SLOT_3](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/i-n-p-u-t_-s-l-o-t_3/) | val [INPUT_SLOT_3](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/i-n-p-u-t_-s-l-o-t_3/): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = 2 |
| [INPUT_SLOT_4](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/i-n-p-u-t_-s-l-o-t_4/) | val [INPUT_SLOT_4](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/i-n-p-u-t_-s-l-o-t_4/): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = 3 |
| [INPUT_SLOT_5](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/i-n-p-u-t_-s-l-o-t_5/) | val [INPUT_SLOT_5](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/i-n-p-u-t_-s-l-o-t_5/): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = 4 |
| [itemStacksResourceHandler](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/item-stacks-resource-handler/) | val [itemStacksResourceHandler](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/item-stacks-resource-handler/): ItemStacksResourceHandler |
| [OUTPUT_SLOT_1](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/o-u-t-p-u-t_-s-l-o-t_1/) | val [OUTPUT_SLOT_1](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/o-u-t-p-u-t_-s-l-o-t_1/): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = 5 |
| [OUTPUT_SLOT_2](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/o-u-t-p-u-t_-s-l-o-t_2/) | val [OUTPUT_SLOT_2](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/o-u-t-p-u-t_-s-l-o-t_2/): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = 6 |

## Functions

| Name | Summary |
|---|---|
| [craftItem](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/craft-item/) | open fun [craftItem](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/craft-item/)() |
| [createMenu](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/create-menu/) | @Nullable<br>open fun [createMenu](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/create-menu/)(containerId: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html), inventory: Inventory, player: Player): @NullableAbstractContainerMenu |
| [drops](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/drops/) | open fun [drops](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/drops/)() |
| [getCurrentRecipe](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/get-current-recipe/) | open fun [getCurrentRecipe](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/get-current-recipe/)(): [Optional](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html)&lt;RecipeHolder&lt;[InfuserRecipe](/docs/api/mods/potion_totems/potion_totems/recipe/infuser-recipe/)&gt;&gt; |
| [getDisplayName](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/get-display-name/) | open fun [getDisplayName](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/get-display-name/)(): Component |
| [hasCraftingFinished](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/has-crafting-finished/) | open fun [hasCraftingFinished](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/has-crafting-finished/)(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) |
| [hasRecipe](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/has-recipe/) | open fun [hasRecipe](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/has-recipe/)(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) |
| [increaseCraftingProgress](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/increase-crafting-progress/) | open fun [increaseCraftingProgress](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/increase-crafting-progress/)() |
| [isOutputSlotEmptyOrReceivable](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/is-output-slot-empty-or-receivable/) | open fun [isOutputSlotEmptyOrReceivable](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/is-output-slot-empty-or-receivable/)(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) |
| [loadAdditional](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/load-additional/) | open fun [loadAdditional](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/load-additional/)(input: ValueInput) |
| [resetProgress](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/reset-progress/) | open fun [resetProgress](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/reset-progress/)() |
| [saveAdditional](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/save-additional/) | open fun [saveAdditional](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/save-additional/)(output: ValueOutput) |
| [tick](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/tick/) | open fun [tick](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/tick/)(level: Level, pPos: BlockPos, pState: BlockState) |
