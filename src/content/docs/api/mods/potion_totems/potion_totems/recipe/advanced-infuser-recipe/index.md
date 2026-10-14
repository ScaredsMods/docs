---
title: "AdvancedInfuserRecipe"
sidebar:
  label: "Overview"
---

```kotlin
class AdvancedInfuserRecipe : Record, Recipe<AdvancedInfuserRecipeInput>
```

## Constructors

| | |
|---|---|
| [AdvancedInfuserRecipe](/docs/api/mods/potion_totems/potion_totems/recipe/advanced-infuser-recipe/advanced-infuser-recipe/) | constructor() |

## Properties

| Name | Summary |
|---|---|
| [CODEC](/docs/api/mods/potion_totems/potion_totems/recipe/advanced-infuser-recipe/c-o-d-e-c/) | val [CODEC](/docs/api/mods/potion_totems/potion_totems/recipe/advanced-infuser-recipe/c-o-d-e-c/): MapCodec&lt;[AdvancedInfuserRecipe](/docs/api/mods/potion_totems/potion_totems/recipe/advanced-infuser-recipe/)&gt; |
| [STREAM_CODEC](/docs/api/mods/potion_totems/potion_totems/recipe/advanced-infuser-recipe/s-t-r-e-a-m_-c-o-d-e-c/) | val [STREAM_CODEC](/docs/api/mods/potion_totems/potion_totems/recipe/advanced-infuser-recipe/s-t-r-e-a-m_-c-o-d-e-c/): StreamCodec&lt;RegistryFriendlyByteBuf, [AdvancedInfuserRecipe](/docs/api/mods/potion_totems/potion_totems/recipe/advanced-infuser-recipe/)&gt; |

## Functions

| Name | Summary |
|---|---|
| [assemble](/docs/api/mods/potion_totems/potion_totems/recipe/advanced-infuser-recipe/assemble/) | open fun [assemble](/docs/api/mods/potion_totems/potion_totems/recipe/advanced-infuser-recipe/assemble/)(advancedInfuserRecipeInput: [AdvancedInfuserRecipeInput](/docs/api/mods/potion_totems/potion_totems/recipe/input/advanced-infuser-recipe-input/)): ItemStack |
| [getIngredients](/docs/api/mods/potion_totems/potion_totems/recipe/advanced-infuser-recipe/get-ingredients/) | open fun [getIngredients](/docs/api/mods/potion_totems/potion_totems/recipe/advanced-infuser-recipe/get-ingredients/)(): NonNullList&lt;Ingredient&gt; |
| [getOutputs](/docs/api/mods/potion_totems/potion_totems/recipe/advanced-infuser-recipe/get-outputs/) | open fun [getOutputs](/docs/api/mods/potion_totems/potion_totems/recipe/advanced-infuser-recipe/get-outputs/)(): [List](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html)&lt;ItemStack&gt; |
| [getSerializer](/docs/api/mods/potion_totems/potion_totems/recipe/advanced-infuser-recipe/get-serializer/) | open fun [getSerializer](/docs/api/mods/potion_totems/potion_totems/recipe/advanced-infuser-recipe/get-serializer/)(): RecipeSerializer&lt;[AdvancedInfuserRecipe](/docs/api/mods/potion_totems/potion_totems/recipe/advanced-infuser-recipe/)&gt; |
| [getType](/docs/api/mods/potion_totems/potion_totems/recipe/advanced-infuser-recipe/get-type/) | open fun [getType](/docs/api/mods/potion_totems/potion_totems/recipe/advanced-infuser-recipe/get-type/)(): RecipeType&lt;[AdvancedInfuserRecipe](/docs/api/mods/potion_totems/potion_totems/recipe/advanced-infuser-recipe/)&gt; |
| [group](/docs/api/mods/potion_totems/potion_totems/recipe/advanced-infuser-recipe/group/) | open fun [group](/docs/api/mods/potion_totems/potion_totems/recipe/advanced-infuser-recipe/group/)(): [String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html) |
| [matches](/docs/api/mods/potion_totems/potion_totems/recipe/advanced-infuser-recipe/matches/) | open fun [matches](/docs/api/mods/potion_totems/potion_totems/recipe/advanced-infuser-recipe/matches/)(advancedInfuserRecipeInput: [AdvancedInfuserRecipeInput](/docs/api/mods/potion_totems/potion_totems/recipe/input/advanced-infuser-recipe-input/), level: Level): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) |
| [placementInfo](/docs/api/mods/potion_totems/potion_totems/recipe/advanced-infuser-recipe/placement-info/) | open fun [placementInfo](/docs/api/mods/potion_totems/potion_totems/recipe/advanced-infuser-recipe/placement-info/)(): PlacementInfo |
| [recipeBookCategory](/docs/api/mods/potion_totems/potion_totems/recipe/advanced-infuser-recipe/recipe-book-category/) | open fun [recipeBookCategory](/docs/api/mods/potion_totems/potion_totems/recipe/advanced-infuser-recipe/recipe-book-category/)(): RecipeBookCategory |
| [showNotification](/docs/api/mods/potion_totems/potion_totems/recipe/advanced-infuser-recipe/show-notification/) | open fun [showNotification](/docs/api/mods/potion_totems/potion_totems/recipe/advanced-infuser-recipe/show-notification/)(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) |
