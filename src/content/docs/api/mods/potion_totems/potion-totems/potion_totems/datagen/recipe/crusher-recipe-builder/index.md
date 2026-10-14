---
title: "CrusherRecipeBuilder"
sidebar:
  label: "Overview"
---

[java]\
open class [CrusherRecipeBuilder](/docs/api/mods/potion_totems/potion-totems/potion_totems/datagen/recipe/crusher-recipe-builder/) : RecipeBuilder

## Properties

| Name | Summary |
|---|---|
| [ROOT_RECIPE_ADVANCEMENT](/docs/api/mods/potion_totems/potion-totems/potion_totems/datagen/recipe/crusher-recipe-builder/#-1221031921%2FProperties%2F-1170581573) | [java]<br>val [ROOT_RECIPE_ADVANCEMENT](/docs/api/mods/potion_totems/potion-totems/potion_totems/datagen/recipe/crusher-recipe-builder/#-1221031921%2FProperties%2F-1170581573): Identifier |

## Functions

| Name | Summary |
|---|---|
| [createCraftingBookInfo](/docs/api/mods/potion_totems/potion-totems/potion_totems/datagen/recipe/crusher-recipe-builder/#615664233%2FFunctions%2F-1170581573) | [java]<br>open fun [createCraftingBookInfo](/docs/api/mods/potion_totems/potion-totems/potion_totems/datagen/recipe/crusher-recipe-builder/#615664233%2FFunctions%2F-1170581573)(category: RecipeCategory, group: @Nullable[String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html)): CraftingRecipe.CraftingBookInfo |
| [createCraftingCommonInfo](/docs/api/mods/potion_totems/potion-totems/potion_totems/datagen/recipe/crusher-recipe-builder/#985214802%2FFunctions%2F-1170581573) | [java]<br>open fun [createCraftingCommonInfo](/docs/api/mods/potion_totems/potion-totems/potion_totems/datagen/recipe/crusher-recipe-builder/#985214802%2FFunctions%2F-1170581573)(showNotification: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)): Recipe.CommonInfo |
| [crushing](/docs/api/mods/potion_totems/potion-totems/potion_totems/datagen/recipe/crusher-recipe-builder/crushing/) | [java]<br>open fun [crushing](/docs/api/mods/potion_totems/potion-totems/potion_totems/datagen/recipe/crusher-recipe-builder/crushing/)(recipeCategory: RecipeCategory, input: Ingredient, outputs: [List](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html)&lt;ItemStackTemplate&gt;): [CrusherRecipeBuilder](/docs/api/mods/potion_totems/potion-totems/potion_totems/datagen/recipe/crusher-recipe-builder/) |
| [defaultId](/docs/api/mods/potion_totems/potion-totems/potion_totems/datagen/recipe/crusher-recipe-builder/default-id/) | [java]<br>open fun [defaultId](/docs/api/mods/potion_totems/potion-totems/potion_totems/datagen/recipe/crusher-recipe-builder/default-id/)(): ResourceKey&lt;Recipe&lt;out [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)&gt;&gt; |
| [determineCraftingBookCategory](/docs/api/mods/potion_totems/potion-totems/potion_totems/datagen/recipe/crusher-recipe-builder/#1971680668%2FFunctions%2F-1170581573) | [java]<br>open fun [determineCraftingBookCategory](/docs/api/mods/potion_totems/potion-totems/potion_totems/datagen/recipe/crusher-recipe-builder/#1971680668%2FFunctions%2F-1170581573)(category: RecipeCategory): CraftingBookCategory |
| [getDefaultRecipeId](/docs/api/mods/potion_totems/potion-totems/potion_totems/datagen/recipe/crusher-recipe-builder/#-1682859678%2FFunctions%2F-1170581573) | [java]<br>open fun [getDefaultRecipeId](/docs/api/mods/potion_totems/potion-totems/potion_totems/datagen/recipe/crusher-recipe-builder/#-1682859678%2FFunctions%2F-1170581573)(result: ItemInstance): ResourceKey&lt;Recipe&lt;out [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)&gt;&gt; |
| [group](/docs/api/mods/potion_totems/potion-totems/potion_totems/datagen/recipe/crusher-recipe-builder/group/) | [java]<br>open fun [group](/docs/api/mods/potion_totems/potion-totems/potion_totems/datagen/recipe/crusher-recipe-builder/group/)(@Nullablegroup: @Nullable[String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html)): RecipeBuilder |
| [save](/docs/api/mods/potion_totems/potion-totems/potion_totems/datagen/recipe/crusher-recipe-builder/save/) | [java]<br>open fun [save](/docs/api/mods/potion_totems/potion-totems/potion_totems/datagen/recipe/crusher-recipe-builder/save/)(output: RecipeOutput, location: ResourceKey&lt;Recipe&lt;out [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)&gt;&gt;) |
| [unlockedBy](/docs/api/mods/potion_totems/potion-totems/potion_totems/datagen/recipe/crusher-recipe-builder/unlocked-by/) | [java]<br>open fun [unlockedBy](/docs/api/mods/potion_totems/potion-totems/potion_totems/datagen/recipe/crusher-recipe-builder/unlocked-by/)(name: [String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html), criterion: Criterion&lt;out [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)&gt;): RecipeBuilder |
