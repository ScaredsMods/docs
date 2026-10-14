---
title: "AbstractTickingBlockEntity"
sidebar:
  label: "Overview"
---

abstract class [AbstractTickingBlockEntity](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/) : BlockEntity, MenuProvider

#### Inheritors

| |
|---|
| [CrusherBlockEntity](/docs/api/mods/potion_totems/potion_totems/block/entity/crusher-block-entity/) |
| [AdvancedInfuserBlockEntity](/docs/api/mods/potion_totems/potion_totems/block/entity/advanced-infuser-block-entity/) |
| [InfuserBlockEntity](/docs/api/mods/potion_totems/potion_totems/block/entity/infuser-block-entity/) |

## Constructors

| | |
|---|---|
| [AbstractTickingBlockEntity](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/abstract-ticking-block-entity/) | constructor(type: BlockEntityType&lt;out [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)&gt;, pos: BlockPos, state: BlockState)constructor(type: BlockEntityType&lt;out [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)&gt;, pos: BlockPos, blockState: BlockState, displayName: Component) |

## Properties

| Name | Summary |
|---|---|
| [displayName](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/display-name/) | val [displayName](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/display-name/): Component |

## Functions

| Name | Summary |
|---|---|
| [canInsertIntoSlot](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/can-insert-into-slot/) | open fun [canInsertIntoSlot](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/can-insert-into-slot/)(outputs: [List](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html)&lt;ItemStack&gt;, itemStacksResourceHandler: ItemStacksResourceHandler): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)<br>open fun [canInsertIntoSlot](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/can-insert-into-slot/)(output: ItemStack, itemStacksResourceHandler: ItemStacksResourceHandler): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) |
| [craftItem](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/craft-item/) | abstract fun [craftItem](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/craft-item/)() |
| [drops](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/drops/) | abstract fun [drops](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/drops/)() |
| [getCurrentRecipe](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/get-current-recipe/) | open fun &lt;[I](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/get-current-recipe/) : RecipeInput?, [R](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/get-current-recipe/) : Recipe&lt;[I](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/get-current-recipe/)&gt;?&gt; [getCurrentRecipe](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/get-current-recipe/)(): [Optional](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html)&lt;RecipeHolder&lt;[R](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/get-current-recipe/)&gt;&gt; |
| [getUpdatePacket](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/get-update-packet/) | @Nullable<br>open fun [getUpdatePacket](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/get-update-packet/)(): @NullablePacket&lt;ClientGamePacketListener&gt; |
| [getUpdateTag](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/get-update-tag/) | open fun [getUpdateTag](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/get-update-tag/)(registries: HolderLookup.Provider): CompoundTag |
| [hasCraftingFinished](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/has-crafting-finished/) | abstract fun [hasCraftingFinished](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/has-crafting-finished/)(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) |
| [hasRecipe](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/has-recipe/) | abstract fun [hasRecipe](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/has-recipe/)(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) |
| [increaseCraftingProgress](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/increase-crafting-progress/) | abstract fun [increaseCraftingProgress](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/increase-crafting-progress/)() |
| [isOutputSlotEmptyOrReceivable](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/is-output-slot-empty-or-receivable/) | abstract fun [isOutputSlotEmptyOrReceivable](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/is-output-slot-empty-or-receivable/)(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) |
| [onDataPacket](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/on-data-packet/) | open fun [onDataPacket](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/on-data-packet/)(net: Connection, valueInput: ValueInput) |
| [resetProgress](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/reset-progress/) | abstract fun [resetProgress](/docs/api/mods/potion_totems/potion_totems/block/entity/abstract-ticking-block-entity/reset-progress/)() |
