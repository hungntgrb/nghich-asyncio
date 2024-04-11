# Breakfast

## Synchronous version

```shell
Start brewCoffee()
  Stop brewCoffee()
        Coffee done!
Start toastBread()
  Stop toastBread()
        Bread done!
Start fryEggsAndHam()
  Stop fryEggsAndHam()
        Eggs and Ham done!
It took 9.01 seconds!
```

## Asynchronous version

```shell
Start brewCoffee()
Start toastBread()
Start fryEggsAndHam()
  Stop toastBread()
  Stop brewCoffee()
        Coffee done!
        Bread done!
  Stop fryEggsAndHam()
        Eggs and Ham done!
It took 4.01 seconds!
```
