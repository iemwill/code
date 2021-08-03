// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.2.0/contracts/token/ERC20/ERC20.sol";

contract dhbwToken is ERC20 {
    constructor() ERC20 ("DHBW-Token", "DHBW"){
        _mint(msg.sender, 1000000 * 10 ** (uint256(decimals())));
    }
}