function Characteristic(displayName, UUID, props) {
  this.displayName = displayName;
  this.UUID = UUID;
  this.iid = null; // assigned by our containing Service
  this.value = null;
  this.status = null;
  this.eventOnlyCharacteristic = false;
  this.props = props || {
    format: null,
    unit: null,
    minValue: null,
    maxValue: null,
    minStep: null,
    perms: []
  };

  this.subscriptions = 0;
}