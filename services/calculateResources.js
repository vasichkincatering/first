function calculateResources(menu) {
  const equipment = [];
  const personnel = [];
  const products = [];

  menu.items.forEach(item => {
    equipment.push(`Equipment for ${item.name}`);
    personnel.push(`Staff for ${item.name}`);
    products.push({ name: item.name, quantity: item.quantity });
  });

  return { equipment, personnel, products };
}

module.exports = calculateResources;
