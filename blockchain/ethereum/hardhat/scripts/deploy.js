async function main() {
  const unlockTime = Math.floor(Date.now() / 1000) + 60; // unlock in 60 seconds
  const Lock = await ethers.getContractFactory("Lock");
  const lock = await Lock.deploy(unlockTime, { value: ethers.parseEther("0.01") });

  console.log("Lock deployed to:", await lock.getAddress());
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});