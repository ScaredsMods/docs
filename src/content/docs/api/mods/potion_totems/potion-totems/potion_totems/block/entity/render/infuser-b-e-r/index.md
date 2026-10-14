---
title: "InfuserBER"
sidebar:
  label: "Overview"
---

[java]\
open class [InfuserBER](/docs/api/mods/potion_totems/potion-totems/potion_totems/block/entity/render/infuser-b-e-r/) : BlockEntityRenderer&lt;[InfuserBlockEntity](/docs/api/mods/potion_totems/potion-totems/potion_totems/block/entity/infuser-block-entity/), [InfuserRenderState](/docs/api/mods/potion_totems/potion-totems/potion_totems/block/entity/render/state/infuser-render-state/)&gt;

## Constructors

| | |
|---|---|
| [InfuserBER](/docs/api/mods/potion_totems/potion-totems/potion_totems/block/entity/render/infuser-b-e-r/infuser-b-e-r/) | [java]<br>constructor(context: BlockEntityRendererProvider.Context) |

## Functions

| Name | Summary |
|---|---|
| [createRenderState](/docs/api/mods/potion_totems/potion-totems/potion_totems/block/entity/render/infuser-b-e-r/create-render-state/) | [java]<br>open fun [createRenderState](/docs/api/mods/potion_totems/potion-totems/potion_totems/block/entity/render/infuser-b-e-r/create-render-state/)(): [InfuserRenderState](/docs/api/mods/potion_totems/potion-totems/potion_totems/block/entity/render/state/infuser-render-state/) |
| [extractRenderState](/docs/api/mods/potion_totems/potion-totems/potion_totems/block/entity/render/infuser-b-e-r/extract-render-state/) | [java]<br>open fun [extractRenderState](/docs/api/mods/potion_totems/potion-totems/potion_totems/block/entity/render/infuser-b-e-r/extract-render-state/)(blockEntity: [InfuserBlockEntity](/docs/api/mods/potion_totems/potion-totems/potion_totems/block/entity/infuser-block-entity/), state: [InfuserRenderState](/docs/api/mods/potion_totems/potion-totems/potion_totems/block/entity/render/state/infuser-render-state/), partialTicks: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html), cameraPosition: Vec3, breakProgress: @NullableModelFeatureRenderer.CrumblingOverlay) |
| [getRenderBoundingBox](/docs/api/mods/potion_totems/potion-totems/potion_totems/block/entity/render/advanced-infuser-b-e-r/#-1459256397%2FFunctions%2F-1170581573) | [java]<br>open fun [getRenderBoundingBox](/docs/api/mods/potion_totems/potion-totems/potion_totems/block/entity/render/advanced-infuser-b-e-r/#-1459256397%2FFunctions%2F-1170581573)(blockEntity: T): AABB |
| [getViewDistance](/docs/api/mods/potion_totems/potion-totems/potion_totems/block/entity/render/advanced-infuser-b-e-r/#-1869325310%2FFunctions%2F-1170581573) | [java]<br>open fun [getViewDistance](/docs/api/mods/potion_totems/potion-totems/potion_totems/block/entity/render/advanced-infuser-b-e-r/#-1869325310%2FFunctions%2F-1170581573)(): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |
| [shouldRender](/docs/api/mods/potion_totems/potion-totems/potion_totems/block/entity/render/advanced-infuser-b-e-r/#26932805%2FFunctions%2F-1170581573) | [java]<br>open fun [shouldRender](/docs/api/mods/potion_totems/potion-totems/potion_totems/block/entity/render/advanced-infuser-b-e-r/#26932805%2FFunctions%2F-1170581573)(blockEntity: T, cameraPosition: Vec3): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) |
| [shouldRenderOffScreen](/docs/api/mods/potion_totems/potion-totems/potion_totems/block/entity/render/advanced-infuser-b-e-r/#-614583520%2FFunctions%2F-1170581573) | [java]<br>open fun [shouldRenderOffScreen](/docs/api/mods/potion_totems/potion-totems/potion_totems/block/entity/render/advanced-infuser-b-e-r/#-614583520%2FFunctions%2F-1170581573)(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) |
| [submit](/docs/api/mods/potion_totems/potion-totems/potion_totems/block/entity/render/infuser-b-e-r/submit/) | [java]<br>open fun [submit](/docs/api/mods/potion_totems/potion-totems/potion_totems/block/entity/render/infuser-b-e-r/submit/)(state: [InfuserRenderState](/docs/api/mods/potion_totems/potion-totems/potion_totems/block/entity/render/state/infuser-render-state/), poseStack: PoseStack, submitNodeCollector: SubmitNodeCollector, camera: CameraRenderState) |
