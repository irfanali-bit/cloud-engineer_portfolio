print("===== CLOUD VM DEPLOYMENT =====")
print("Starting deployment...")

for i in range(1, 6):
    print("Creating VM", i)

print("Deployment completed!")


print("----- VM CREATION WITH CONTINUE -----")

for i in range(1, 6):
    if i == 3:
        continue

    print("Creating VM", i)

print("Deployment completed!")


print("----- VM CHECK -----")

for i in range(1, 6):
    if i == 4:
        break

    print("Checking VM", i)