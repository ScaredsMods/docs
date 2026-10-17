---
title: "apply"
---

```kotlin
open fun apply()
```

A method that must be called if you want to actually use the resources generated. It works purely client-side, as it should, and adds your pack to the pack repository, ready to be loaded. It can be loaded anytime a client-side event happens, like pressing a key.
