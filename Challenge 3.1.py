def linearsearchproducts(productslist, targetproducts):
  indices = []
  for index, product in enumerate(productslist):
    if product == targetproducts:
      indices.append(index)
  return indices


products = ["yamaha", "ktm", "honda", "bajaj", "pulsar", "ktm"]
target = "ktm"
target = "suzuki"
final = linearsearchproducts(products, target)
print(final)
