---
title: "InfuserRecipe"
sidebar:
  label: "Overview"
---

[java]\
class [InfuserRecipe](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/infuser-recipe/) : [Record](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Record.html), Recipe&lt;[InfuserRecipeInput](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/input/infuser-recipe-input/)&gt;

## Constructors

| | |
|---|---|
| [InfuserRecipe](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/infuser-recipe/infuser-recipe/) | [java]<br>constructor() |

## Properties

| Name | Summary |
|---|---|
| [CODEC](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/infuser-recipe/c-o-d-e-c/) | [java]<br>val [CODEC](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/infuser-recipe/c-o-d-e-c/): MapCodec&lt;[InfuserRecipe](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/infuser-recipe/)&gt;<br>val [CODEC](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/crusher-recipe/#1807178120%2FProperties%2F-1170581573): Codec&lt;Recipe&lt;out [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)&gt;&gt; |
| [CONDITIONAL_CODEC](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/crusher-recipe/#772681985%2FProperties%2F-1170581573) | [java]<br>val [CONDITIONAL_CODEC](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/crusher-recipe/#772681985%2FProperties%2F-1170581573): Codec&lt;[Optional](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html)&lt;WithConditions&lt;Recipe&lt;out [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)&gt;&gt;&gt;&gt; |
| [KEY_CODEC](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/crusher-recipe/#1444124424%2FProperties%2F-1170581573) | [java]<br>val [KEY_CODEC](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/crusher-recipe/#1444124424%2FProperties%2F-1170581573): Codec&lt;ResourceKey&lt;Recipe&lt;out [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)&gt;&gt;&gt; |
| [STREAM_CODEC](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/infuser-recipe/s-t-r-e-a-m_-c-o-d-e-c/) | [java]<br>val [STREAM_CODEC](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/infuser-recipe/s-t-r-e-a-m_-c-o-d-e-c/): StreamCodec&lt;RegistryFriendlyByteBuf, [InfuserRecipe](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/infuser-recipe/)&gt;<br>val [STREAM_CODEC](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/crusher-recipe/#-1824298747%2FProperties%2F-1170581573): StreamCodec&lt;RegistryFriendlyByteBuf, Recipe&lt;out [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)&gt;&gt; |

## Functions

| Name | Summary |
|---|---|
| [assemble](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/infuser-recipe/assemble/) | [java]<br>open fun [assemble](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/infuser-recipe/assemble/)(infuserRecipeInput: [InfuserRecipeInput](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/input/infuser-recipe-input/)): ItemStack |
| [display](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/crusher-recipe/#1501977084%2FFunctions%2F-1170581573) | [java]<br>open fun [display](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/crusher-recipe/#1501977084%2FFunctions%2F-1170581573)(): [List](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html)&lt;RecipeDisplay&gt; |
| [equals](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/input/infuser-recipe-input/#-1797860926%2FFunctions%2F-1170581573) | [java]<br>abstract fun [equals](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/input/infuser-recipe-input/#-1797860926%2FFunctions%2F-1170581573)(p: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) |
| [getIngredients](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/infuser-recipe/get-ingredients/) | [java]<br>open fun [getIngredients](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/infuser-recipe/get-ingredients/)(): NonNullList&lt;Ingredient&gt; |
| [getOutputs](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/infuser-recipe/get-outputs/) | [java]<br>open fun [getOutputs](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/infuser-recipe/get-outputs/)(): [List](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html)&lt;ItemStack&gt; |
| [getSerializer](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/infuser-recipe/get-serializer/) | [java]<br>open fun [getSerializer](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/infuser-recipe/get-serializer/)(): RecipeSerializer&lt;[InfuserRecipe](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/infuser-recipe/)&gt; |
| [getType](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/infuser-recipe/get-type/) | [java]<br>open fun [getType](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/infuser-recipe/get-type/)(): RecipeType&lt;[InfuserRecipe](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/infuser-recipe/)&gt; |
| [group](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/infuser-recipe/group/) | [java]<br>open fun [group](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/infuser-recipe/group/)(): [String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html) |
| [hashCode](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/input/infuser-recipe-input/#1761002009%2FFunctions%2F-1170581573) | [java]<br>abstract fun [hashCode](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/input/infuser-recipe-input/#1761002009%2FFunctions%2F-1170581573)(): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |
| [isSpecial](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/crusher-recipe/#-17628433%2FFunctions%2F-1170581573) | [java]<br>open fun [isSpecial](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/crusher-recipe/#-17628433%2FFunctions%2F-1170581573)(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) |
| [matches](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/infuser-recipe/matches/) | [java]<br>open fun [matches](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/infuser-recipe/matches/)(infuserRecipeInput: [InfuserRecipeInput](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/input/infuser-recipe-input/), level: Level): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) |
| [placementInfo](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/infuser-recipe/placement-info/) | [java]<br>open fun [placementInfo](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/infuser-recipe/placement-info/)(): PlacementInfo |
| [recipeBookCategory](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/infuser-recipe/recipe-book-category/) | [java]<br>open fun [recipeBookCategory](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/infuser-recipe/recipe-book-category/)(): RecipeBookCategory |
| [showNotification](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/infuser-recipe/show-notification/) | [java]<br>open fun [showNotification](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/infuser-recipe/show-notification/)(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) |
| [toString](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/input/infuser-recipe-input/#1582835944%2FFunctions%2F-1170581573) | [java]<br>abstract fun [toString](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/input/infuser-recipe-input/#1582835944%2FFunctions%2F-1170581573)(): [String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html) |
