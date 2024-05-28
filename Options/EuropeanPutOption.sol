// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

/**
 * The EuropeanPutOption contract holds the amount unit of the underlying asset multiplied with the 
 * strike Price k in ETH. The Contract als has an expiration date given in days, starting from 
 * creating the contract. One can trade the Option contract in the Basecurrency ETH until the given 
 * date and then the current holder can determine wether to use the option or not.
 * 0xc3577e1BF219c041306dDa4689a1D1Fb531329A0
 */
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/IERC20.sol";

contract CallOption {
  address public initialOwner;

  address public asset;
  uint public assetAmount;
  uint public strikePrice;
  uint public expirationInDays;
  uint public startTimestamp;

  bool public active;
  bool public toSell;
  uint public sellPrice;

  address public owner;

  event NewOwner(address newOwner);

  constructor(address _asset, uint _assetAmount, uint _strikePrice, uint _expirationInDays) {
    initialOwner = msg.sender;
    owner = msg.sender;
    active = false;
    toSell = false;
    asset = _asset;
    assetAmount = _assetAmount;
    strikePrice = _strikePrice;
    expirationInDays = _expirationInDays;
    startTimestamp = block.timestamp;
  }

  function activateOption () public payable override returns(bool) {
    if(msg.value == assetAmount * strikePrice) {
      active = true;
      return true;
    } else {
      return false;
    }
  }

  function activateSelling (uint _sellPrice) public override returns(bool) {
    require(active && msg.sender == owner, "You are not the owner of the Option Contract or the Option is not active yet.");
    sellPrice = _sellPrice;
    toSell = true;
    return true;
  }

  function cancelSelling() public override returns(bool) {
    require(active && msg.sender == owner, "You are not the owner of the Option Contract or the Option is not active yet.");
    toSell = false;
    return true;
  }

  function buyOption () public payable override returns(bool) {
    require(msg.value == sellPrice, "The transaction does not include the given sell price.");
    
    if (toSell && active && block.timestamp < startTimestamp + expirationInDays * 1 days) {
      payable(owner).transfer(address(this).balance);
      owner = msg.sender;
      emit NewOwner(owner);
      return true;
    } else {
      return false;
    }
  }

  function useOption () public returns(bool) {
    if(msg.sender == owner && active && block.timestamp >= startTimestamp + expirationInDays * 1 days)
    {
      if(IERC20(asset).balanceOf(address(this)) == assetAmount){
        IERC20(asset).transfer(initialOwner, assetAmount);
        payable(owner).transfer(address(this).balance);
        return true;
      } else {
        payable(initialOwner).transfer(address(this).balance);
        return true;
      }
    } else {
      return false;
    }
  }

  function emptyAll() public returns(bool) {
    require(msg.sender == initialOwner && block.timestamp > startTimestamp + expirationInDays * 1 days + 21 days);
    IERC20(asset).transfer(initialOwner, IERC20(asset).balanceOf(address(this)));
    payable(initialOwner).transfer(address(this).balance);
    return true;
  }
}