// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.28;

// Uncomment this line to use console.log
// import "hardhat/console.sol";

contract Lock {
  uint public unlockTime;
  address payable public owner;

  event Withdrawal(uint amount, uint when);

  constructor(uint _unlockTime) payable {
    require(
      block.timestamp < _unlockTime,
      "Unlock time should be in the future"
    );

    unlockTime = _unlockTime;
    owner = payable(msg.sender);
  }

  function withdraw() public {
    // Uncomment this line, and the import of "hardhat/console.sol", to print a log in your terminal
    // console.log("Unlock time is %o and block timestamp is %o", unlockTime, block.timestamp);

    require(block.timestamp >= unlockTime, "You can't withdraw yet");
    require(msg.sender == owner, "You aren't the owner");

    uint256 balance = address(this).balance;
    require(balance > 0, "No ETH to withdraw");

    emit Withdrawal(address(this).balance, block.timestamp);

    (bool success, ) = owner.call{value: address(this).balance}("");
    require(success, "ETH transfer failed");
  }
}
