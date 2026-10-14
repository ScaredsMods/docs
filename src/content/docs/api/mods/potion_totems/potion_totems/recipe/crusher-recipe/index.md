---
title: "CrusherRecipe"
sidebar:
  label: "Overview"
---

```kotlin
class CrusherRecipe : Record, Recipe<CrusherRecipeInput>
```

## Constructors

| | |
|---|---|
| [CrusherRecipe](/docs/api/mods/potion_totems/potion_totems/recipe/crusher-recipe/crusher-recipe/) | constructor() |

## Properties

| Name | Summary |
|---|---|
| [CODEC](/docs/api/mods/potion_totems/potion_totems/recipe/crusher-recipe/c-o-d-e-c/) | open var [CODEC](/docs/api/mods/potion_totems/potion_totems/recipe/crusher-recipe/c-o-d-e-c/): MapCodec&lt;[CrusherRecipe](/docs/api/mods/potion_totems/potion_totems/recipe/crusher-recipe/)&gt; |
| [STREAM_CODEC](/docs/api/mods/potion_totems/potion_totems/recipe/crusher-recipe/s-t-r-e-a-m_-c-o-d-e-c/) | open var [STREAM_CODEC](/docs/api/mods/potion_totems/potion_totems/recipe/crusher-recipe/s-t-r-e-a-m_-c-o-d-e-c/): StreamCodec&lt;RegistryFriendlyByteBuf, [CrusherRecipe](/docs/api/mods/potion_totems/potion_totems/recipe/crusher-recipe/)&gt; |

## Functions

| Name | Summary |
|---|---|
| [assemble](/docs/api/mods/potion_totems/potion_totems/recipe/crusher-recipe/assemble/) | open fun [assemble](/docs/api/mods/potion_totems/potion_totems/recipe/crusher-recipe/assemble/)(input: [CrusherRecipeInput](/docs/api/mods/potion_totems/potion_totems/recipe/input/crusher-recipe-input/)): ItemStack |
| [getIngredients](/docs/api/mods/potion_totems/potion_totems/recipe/crusher-recipe/get-ingredients/) | open fun [getIngredients](/docs/api/mods/potion_totems/potion_totems/recipe/crusher-recipe/get-ingredients/)(): NonNullList&lt;Ingredient&gt; |
| [getOutputs](/docs/api/mods/potion_totems/potion_totems/recipe/crusher-recipe/get-outputs/) | open fun [getOutputs](/docs/api/mods/potion_totems/potion_totems/recipe/crusher-recipe/get-outputs/)(): [List](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html)&lt;ItemStack&gt; |
| [getSerializer](/docs/api/mods/potion_totems/potion_totems/recipe/crusher-recipe/get-serializer/) | open fun [getSerializer](/docs/api/mods/potion_totems/potion_totems/recipe/crusher-recipe/get-serializer/)(): RecipeSerializer&lt;[CrusherRecipe](/docs/api/mods/potion_totems/potion_totems/recipe/crusher-recipe/)&gt; |
| [getType](/docs/api/mods/potion_totems/potion_totems/recipe/crusher-recipe/get-type/) | open fun [getType](/docs/api/mods/potion_totems/potion_totems/recipe/crusher-recipe/get-type/)(): RecipeType&lt;[CrusherRecipe](/docs/api/mods/potion_totems/potion_totems/recipe/crusher-recipe/)&gt; |
| [group](/docs/api/mods/potion_totems/potion_totems/recipe/crusher-recipe/group/) | open fun [group](/docs/api/mods/potion_totems/potion_totems/recipe/crusher-recipe/group/)(): [String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html) |
| [matches](/docs/api/mods/potion_totems/potion_totems/recipe/crusher-recipe/matches/) | open fun [matches](/docs/api/mods/potion_totems/potion_totems/recipe/crusher-recipe/matches/)(input: [CrusherRecipeInput](/docs/api/mods/potion_totems/potion_totems/recipe/input/crusher-recipe-input/), level: Level): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) |
| [placementInfo](/docs/api/mods/potion_totems/potion_totems/recipe/crusher-recipe/placement-info/) | open fun [placementInfo](/docs/api/mods/potion_totems/potion_totems/recipe/crusher-recipe/placement-info/)(): PlacementInfo |
| [recipeBookCategory](/docs/api/mods/potion_totems/potion_totems/recipe/crusher-recipe/recipe-book-category/) | open fun [recipeBookCategory](/docs/api/mods/potion_totems/potion_totems/recipe/crusher-recipe/recipe-book-category/)(): RecipeBookCategory |
| [showNotification](/docs/api/mods/potion_totems/potion_totems/recipe/crusher-recipe/show-notification/) | open fun [showNotification](/docs/api/mods/potion_totems/potion_totems/recipe/crusher-recipe/show-notification/)(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) |
