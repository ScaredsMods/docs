---
title: "InfuserBlock"
sidebar:
  label: "Overview"
---

```kotlin
open class InfuserBlock : AbstractHorizontalBlock
```

## Constructors

| | |
|---|---|
| [InfuserBlock](/docs/api/mods/potion_totems/potion_totems/block/infuser-block/infuser-block/) | constructor(properties: BlockBehaviour.Properties) |

## Properties

| Name | Summary |
|---|---|
| [CODEC](/docs/api/mods/potion_totems/potion_totems/block/infuser-block/c-o-d-e-c/) | val [CODEC](/docs/api/mods/potion_totems/potion_totems/block/infuser-block/c-o-d-e-c/): MapCodec&lt;[InfuserBlock](/docs/api/mods/potion_totems/potion_totems/block/infuser-block/)&gt; |
| [SHAPE](/docs/api/mods/potion_totems/potion_totems/block/infuser-block/s-h-a-p-e/) | val [SHAPE](/docs/api/mods/potion_totems/potion_totems/block/infuser-block/s-h-a-p-e/): VoxelShape |

## Functions

| Name | Summary |
|---|---|
| [getLightEmission](/docs/api/mods/potion_totems/potion_totems/block/infuser-block/get-light-emission/) | open fun [getLightEmission](/docs/api/mods/potion_totems/potion_totems/block/infuser-block/get-light-emission/)(state: BlockState, level: BlockGetter, pos: BlockPos): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |
| [getRenderShape](/docs/api/mods/potion_totems/potion_totems/block/infuser-block/get-render-shape/) | open fun [getRenderShape](/docs/api/mods/potion_totems/potion_totems/block/infuser-block/get-render-shape/)(blockState: BlockState): RenderShape |
| [getTicker](/docs/api/mods/potion_totems/potion_totems/block/infuser-block/get-ticker/) | @Nullable<br>open fun &lt;[T](/docs/api/mods/potion_totems/potion_totems/block/infuser-block/get-ticker/) : BlockEntity?&gt; [getTicker](/docs/api/mods/potion_totems/potion_totems/block/infuser-block/get-ticker/)(level: Level, state: BlockState, blockEntityType: BlockEntityType&lt;[T](/docs/api/mods/potion_totems/potion_totems/block/infuser-block/get-ticker/)&gt;): @NullableBlockEntityTicker&lt;[T](/docs/api/mods/potion_totems/potion_totems/block/infuser-block/get-ticker/)&gt; |
| [newBlockEntity](/docs/api/mods/potion_totems/potion_totems/block/infuser-block/new-block-entity/) | @Nullable<br>open fun [newBlockEntity](/docs/api/mods/potion_totems/potion_totems/block/infuser-block/new-block-entity/)(pos: BlockPos, state: BlockState): @NullableBlockEntity |
