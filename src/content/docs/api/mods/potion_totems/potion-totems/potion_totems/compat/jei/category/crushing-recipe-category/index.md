---
title: "CrushingRecipeCategory"
sidebar:
  label: "Overview"
---

[java]\
open class [CrushingRecipeCategory](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/) : IRecipeCategory&lt;RecipeHolder&lt;[CrusherRecipe](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/crusher-recipe/)&gt;&gt;

## Constructors

| | |
|---|---|
| [CrushingRecipeCategory](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/crushing-recipe-category/) | [java]<br>constructor(helper: IGuiHelper) |

## Properties

| Name | Summary |
|---|---|
| [icon](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/icon/) | [java]<br>@get:Nullable<br>val [icon](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/icon/): IDrawable |

## Functions

| Name | Summary |
|---|---|
| [createRecipeExtras](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/#906523810%2FFunctions%2F-1170581573) | [java]<br>open fun [createRecipeExtras](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/#906523810%2FFunctions%2F-1170581573)(builder: IRecipeExtrasBuilder, recipe: T, focuses: IFocusGroup) |
| [draw](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/draw/) | [java]<br>open fun [draw](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/draw/)(recipe: RecipeHolder&lt;[CrusherRecipe](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/crusher-recipe/)&gt;, recipeSlotsView: IRecipeSlotsView, guiGraphics: GuiGraphicsExtractor, mouseX: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html), mouseY: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)) |
| [getCodec](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/#610874311%2FFunctions%2F-1170581573) | [java]<br>open fun [getCodec](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/#610874311%2FFunctions%2F-1170581573)(codecHelper: ICodecHelper, recipeManager: IRecipeManager): Codec&lt;T&gt; |
| [getHeight](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/get-height/) | [java]<br>open fun [getHeight](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/get-height/)(): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |
| [getIcon](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/#885454531%2FFunctions%2F-1170581573) | [java]<br>abstract fun [getIcon](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/#885454531%2FFunctions%2F-1170581573)(): @NullableIDrawable |
| [getIdentifier](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/#299868219%2FFunctions%2F-1170581573) | [java]<br>open fun [getIdentifier](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/#299868219%2FFunctions%2F-1170581573)(recipe: T): @NullableIdentifier |
| [getRecipeType](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/get-recipe-type/) | [java]<br>open fun [getRecipeType](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/get-recipe-type/)(): IRecipeType&lt;RecipeHolder&lt;[CrusherRecipe](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/crusher-recipe/)&gt;&gt; |
| [getRegistryName](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/#1233518330%2FFunctions%2F-1170581573) | [java]<br>open fun [getRegistryName](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/#1233518330%2FFunctions%2F-1170581573)(recipe: T): @NullableIdentifier |
| [getTitle](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/get-title/) | [java]<br>open fun [getTitle](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/get-title/)(): Component |
| [getTooltip](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/#1791945187%2FFunctions%2F-1170581573) | [java]<br>open fun [getTooltip](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/#1791945187%2FFunctions%2F-1170581573)(tooltip: ITooltipBuilder, recipe: T, recipeSlotsView: IRecipeSlotsView, mouseX: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html), mouseY: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)) |
| [getWidth](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/get-width/) | [java]<br>open fun [getWidth](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/get-width/)(): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |
| [isHandled](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/#-1238567410%2FFunctions%2F-1170581573) | [java]<br>open fun [isHandled](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/#-1238567410%2FFunctions%2F-1170581573)(recipe: T): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) |
| [needsRecipeBorder](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/#-2121858085%2FFunctions%2F-1170581573) | [java]<br>open fun [needsRecipeBorder](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/#-2121858085%2FFunctions%2F-1170581573)(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) |
| [onDisplayedIngredientsUpdate](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/#-51794030%2FFunctions%2F-1170581573) | [java]<br>open fun [onDisplayedIngredientsUpdate](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/#-51794030%2FFunctions%2F-1170581573)(recipe: T, recipeSlots: [List](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html)&lt;IRecipeSlotDrawable&gt;, focuses: IFocusGroup) |
| [setRecipe](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/set-recipe/) | [java]<br>open fun [setRecipe](/docs/api/mods/potion_totems/potion-totems/potion_totems/compat/jei/category/crushing-recipe-category/set-recipe/)(builder: IRecipeLayoutBuilder, recipe: RecipeHolder&lt;[CrusherRecipe](/docs/api/mods/potion_totems/potion-totems/potion_totems/recipe/crusher-recipe/)&gt;, focuses: IFocusGroup) |
