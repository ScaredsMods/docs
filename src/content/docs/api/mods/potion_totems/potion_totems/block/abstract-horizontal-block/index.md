---
title: "AbstractHorizontalBlock"
sidebar:
  label: "Overview"
---

abstract class [AbstractHorizontalBlock](/docs/api/mods/potion_totems/potion_totems/block/abstract-horizontal-block/) : BaseEntityBlock

#### Inheritors

| |
|---|
| [InfuserBlock](/docs/api/mods/potion_totems/potion_totems/block/infuser-block/) |
| [CrusherBlock](/docs/api/mods/potion_totems/potion_totems/block/crusher-block/) |
| [AdvancedInfuserBlock](/docs/api/mods/potion_totems/potion_totems/block/advanced-infuser-block/) |

## Constructors

| | |
|---|---|
| [AbstractHorizontalBlock](/docs/api/mods/potion_totems/potion_totems/block/abstract-horizontal-block/abstract-horizontal-block/) | constructor(properties: BlockBehaviour.Properties, shape: VoxelShape) |

## Properties

| Name | Summary |
|---|---|
| [HORIZONTAL_FACING](/docs/api/mods/potion_totems/potion_totems/block/abstract-horizontal-block/h-o-r-i-z-o-n-t-a-l_-f-a-c-i-n-g/) | val [HORIZONTAL_FACING](/docs/api/mods/potion_totems/potion_totems/block/abstract-horizontal-block/h-o-r-i-z-o-n-t-a-l_-f-a-c-i-n-g/): EnumProperty&lt;Direction&gt; |

## Functions

| Name | Summary |
|---|---|
| [getStateForPlacement](/docs/api/mods/potion_totems/potion_totems/block/abstract-horizontal-block/get-state-for-placement/) | open fun [getStateForPlacement](/docs/api/mods/potion_totems/potion_totems/block/abstract-horizontal-block/get-state-for-placement/)(context: BlockPlaceContext): BlockState |
| [mirror](/docs/api/mods/potion_totems/potion_totems/block/abstract-horizontal-block/mirror/) | @NonNull<br>open fun [mirror](/docs/api/mods/potion_totems/potion_totems/block/abstract-horizontal-block/mirror/)(state: BlockState, mirrorIn: Mirror): @NonNullBlockState |
| [onDestroyedByPlayer](/docs/api/mods/potion_totems/potion_totems/block/abstract-horizontal-block/on-destroyed-by-player/) | open fun [onDestroyedByPlayer](/docs/api/mods/potion_totems/potion_totems/block/abstract-horizontal-block/on-destroyed-by-player/)(state: BlockState, level: Level, pos: BlockPos, player: Player, toolStack: ItemStack, willHarvest: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html), fluid: FluidState): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) |
| [rotate](/docs/api/mods/potion_totems/potion_totems/block/abstract-horizontal-block/rotate/) | @NonNull<br>open fun [rotate](/docs/api/mods/potion_totems/potion_totems/block/abstract-horizontal-block/rotate/)(state: BlockState, direction: Rotation): @NonNullBlockState |
