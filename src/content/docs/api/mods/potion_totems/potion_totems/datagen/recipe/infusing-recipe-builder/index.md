---
title: "InfusingRecipeBuilder"
sidebar:
  label: "Overview"
---

```kotlin
open class InfusingRecipeBuilder : RecipeBuilder
```

## Functions

| Name | Summary |
|---|---|
| [defaultId](/docs/api/mods/potion_totems/potion_totems/datagen/recipe/infusing-recipe-builder/default-id/) | open fun [defaultId](/docs/api/mods/potion_totems/potion_totems/datagen/recipe/infusing-recipe-builder/default-id/)(): ResourceKey&lt;Recipe&lt;out [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)&gt;&gt; |
| [group](/docs/api/mods/potion_totems/potion_totems/datagen/recipe/infusing-recipe-builder/group/) | open fun [group](/docs/api/mods/potion_totems/potion_totems/datagen/recipe/infusing-recipe-builder/group/)(@Nullablegroup: @Nullable[String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html)): RecipeBuilder |
| [infusing](/docs/api/mods/potion_totems/potion_totems/datagen/recipe/infusing-recipe-builder/infusing/) | open fun [infusing](/docs/api/mods/potion_totems/potion_totems/datagen/recipe/infusing-recipe-builder/infusing/)(category: RecipeCategory, inputItem: [List](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html)&lt;Ingredient&gt;, items: [List](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html)&lt;ItemStackTemplate&gt;): [InfusingRecipeBuilder](/docs/api/mods/potion_totems/potion_totems/datagen/recipe/infusing-recipe-builder/) |
| [save](/docs/api/mods/potion_totems/potion_totems/datagen/recipe/infusing-recipe-builder/save/) | open fun [save](/docs/api/mods/potion_totems/potion_totems/datagen/recipe/infusing-recipe-builder/save/)(output: RecipeOutput, location: ResourceKey&lt;Recipe&lt;out [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)&gt;&gt;) |
| [unlockedBy](/docs/api/mods/potion_totems/potion_totems/datagen/recipe/infusing-recipe-builder/unlocked-by/) | open fun [unlockedBy](/docs/api/mods/potion_totems/potion_totems/datagen/recipe/infusing-recipe-builder/unlocked-by/)(name: [String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html), criterion: Criterion&lt;out [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)&gt;): RecipeBuilder |
