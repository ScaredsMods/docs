---
title: "InfusingRecipeCategory"
sidebar:
  label: "Overview"
---

```kotlin
open class InfusingRecipeCategory : IRecipeCategory<RecipeHolder<InfuserRecipe>>
```

## Constructors

| | |
|---|---|
| [InfusingRecipeCategory](/docs/api/mods/potion_totems/potion_totems/compat/jei/category/infusing-recipe-category/infusing-recipe-category/) | constructor(helper: IGuiHelper) |

## Properties

| Name | Summary |
|---|---|
| [icon](/docs/api/mods/potion_totems/potion_totems/compat/jei/category/infusing-recipe-category/icon/) | @get:Nullable<br>val [icon](/docs/api/mods/potion_totems/potion_totems/compat/jei/category/infusing-recipe-category/icon/): IDrawable |

## Functions

| Name | Summary |
|---|---|
| [draw](/docs/api/mods/potion_totems/potion_totems/compat/jei/category/infusing-recipe-category/draw/) | open fun [draw](/docs/api/mods/potion_totems/potion_totems/compat/jei/category/infusing-recipe-category/draw/)(recipe: RecipeHolder&lt;[InfuserRecipe](/docs/api/mods/potion_totems/potion_totems/recipe/infuser-recipe/)&gt;, recipeSlotsView: IRecipeSlotsView, guiGraphics: GuiGraphicsExtractor, mouseX: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html), mouseY: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)) |
| [getHeight](/docs/api/mods/potion_totems/potion_totems/compat/jei/category/infusing-recipe-category/get-height/) | open fun [getHeight](/docs/api/mods/potion_totems/potion_totems/compat/jei/category/infusing-recipe-category/get-height/)(): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |
| [getRecipeType](/docs/api/mods/potion_totems/potion_totems/compat/jei/category/infusing-recipe-category/get-recipe-type/) | open fun [getRecipeType](/docs/api/mods/potion_totems/potion_totems/compat/jei/category/infusing-recipe-category/get-recipe-type/)(): IRecipeType&lt;RecipeHolder&lt;[InfuserRecipe](/docs/api/mods/potion_totems/potion_totems/recipe/infuser-recipe/)&gt;&gt; |
| [getTitle](/docs/api/mods/potion_totems/potion_totems/compat/jei/category/infusing-recipe-category/get-title/) | open fun [getTitle](/docs/api/mods/potion_totems/potion_totems/compat/jei/category/infusing-recipe-category/get-title/)(): Component |
| [getWidth](/docs/api/mods/potion_totems/potion_totems/compat/jei/category/infusing-recipe-category/get-width/) | open fun [getWidth](/docs/api/mods/potion_totems/potion_totems/compat/jei/category/infusing-recipe-category/get-width/)(): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |
| [setRecipe](/docs/api/mods/potion_totems/potion_totems/compat/jei/category/infusing-recipe-category/set-recipe/) | open fun [setRecipe](/docs/api/mods/potion_totems/potion_totems/compat/jei/category/infusing-recipe-category/set-recipe/)(builder: IRecipeLayoutBuilder, recipe: RecipeHolder&lt;[InfuserRecipe](/docs/api/mods/potion_totems/potion_totems/recipe/infuser-recipe/)&gt;, focuses: IFocusGroup) |
