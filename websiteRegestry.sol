pragma solidity >=0.8.0;
/**
 * The websiteRegestry contract is a small piece of codelines to
 * register machines calling a servers hosted code of so called websites..
 * SPDX-License-Identifier: MIT
 */
contract websiteRegistry {
	address internal _registrator;
	mapping (string => uint256[]) register;
	modifier allowance(address inputAddress) { 
		require (_registrator == inputAddress); 
		_; 
	}
  	constructor() {
    	_registrator = msg.sender;
  	}
  	function register (string calldata ip) public allowance(msg.sender) returns(bool) {
  	    uint256 input = block.timestamp;
  		register[ip].push(input);
  		return true;
  	}
  	function getVisits (string calldata ip) public view returns(uint256[] memory) {
  		string calldata _ip = ip;
  		uint256[] memory _res;
  		_res = register[_ip];
  		return _res;
  	}
}
